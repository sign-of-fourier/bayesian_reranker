from flask import Flask, Response,send_file, send_from_directory, request, make_response
import pandas as pd
import openai
from azure.core.credentials import AzureKeyCredential
import more_itertools
import chromadb
import pickle
import random
from multiprocessing import Pool
from bayesian_reranker import batch_bayesian_optimization as bbo
from bayesian_reranker.prompt_library import wiki_demo as wd
import string
import asyncio
import re
import os
from bayesian_reranker import webpages as wp


app = Flask(__name__, static_folder='data')





hidden = "<input type=hidden name=\"{}\" value=\"{}\"></input>\n"

#@app.route(["/search_chorma", "/bayes_optimization"], methods=['POST'])

def make_sidebar(K):
    sidebar = '<table>'
    for k in K.keys():
        sidebar += "<tr><td>{}</td><td>{}</td></tr>".format(k, K[k])
    return sidebar + "</table>"

@app.route("/optimize", methods=['POST'])
def optimize():
    path = '/tmp/' + request.form['session_id']
    with open(path + '.mbd','rb') as f:
        combined_embeddings = pickle.load(f)

    with open(path + '.text','rb') as f:
        combined_text = pickle.load(f)
    files = os.listdir('/tmp')

    if request.form['session_id'] + '.scr' in files:

        with open(path + '.scr', 'rb') as f:
            scored_answers = pickle.load(f)

        B = bbo.best_batch_finder(400, 4)
        x2id, unscored_embeddings = B.fit(scored_answers, combined_embeddings)
        B.create_batches(unscored_embeddings)
        try:
            best_idx = B.get_best_batch()
        except Exception as e:
            print(str(e))
            best_idx = random.randint(0, len(B.batch_idx)-1)
        
        keys = [x2id[s] for s in B.batch_idx[best_idx]]
    else:
        scored_answers = {}
        keys = random.sample([s for s in combined_text.keys()], 10)

    parameters = [{'id': i, 'session_id': request.form['session_id'],
                   'system': "You are a librarian. Your job is to determine if a reference is relevant to a query",
                   'user': wd.relevance_prompt.format(request.form['improved_question'], combined_text[s])} for i,s in enumerate(keys)]

    loop = asyncio.new_event_loop()
    tasks = [loop.create_task(bbo.async_call_gpt(p)) for p in parameters]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    answers = []
    for t in range(len(keys)):
        with open('/tmp/' + request.form['session_id'] + f'.{t}', 'r') as f:
            answers.append(f.read())

    for k, q, t in zip(keys, [bbo.x_relevance(a) for a in answers], answers):
        if q > 0:
            scored_answers[k] = q
        else:
            print(q, t)

    df = pd.DataFrame({'id': [s for s in scored_answers.keys()],
                       'score': [scored_answers[s] for s in scored_answers.keys()]})
    relevant_ids = []
    for x in df.sort_values('score', ascending = False).head(3)['id']:
        relevant_ids += x.split('_')

    references = "\n\n".join([f"page {i}:\n" + combined_text[i] for i in set(relevant_ids)])
    final_answer = bbo.call_gpt({'system': 'You are a helpful assistaint.',
                                  'user': wd.rag.format(request.form['improved_question'], references)})

    print(df)

    with open(path + '.scr', 'wb') as f:
        pickle.dump(scored_answers, f)

    sidebar = make_sidebar({'scored_answers': len(scored_answers.keys()),
                            'total answers': len(combined_embeddings.keys())})
    return wp.optimization_page.format(wp.style, wp.navbar, sidebar, re.sub("\n", "\n<br>", request.form['improved_question']), 
                                       re.sub("\"", "", request.form['improved_question']),
                                       'Answer', re.sub("\n", "<br>\n", final_answer), 
                                       hidden.format('session_id', request.form['session_id']), wp.script)

@app.route("/improve_question", methods=['POST'])
def improve_question():
    improved_question = bbo.call_gpt({'system': 'You are a filing clerk. Your job is come up wi', 
                                                                          'user':  wd.improve_query + request.form['query']})
    print(improved_question)
    search_terms = bbo.call_gpt({'system': 'You are a filing clerk. Your job is come up with search terms to help find answers to queries', 
                                 'user': wd.search_term_prompt + improved_question})


    chroma_client = chromadb.PersistentClient(path="mini_wiki")
    collection = chroma_client.get_collection(name='query')
    try:
        search_results = collection.query(
            query_texts = eval(search_terms),
            n_results = 10
        )
    except Exception as e:
        return str(e)
    #search_terms_hidden = ''
    #for i, s in enumerate(eval(search_terms)):
    #    search_terms_hidden += hidden.format(f'search_terms-{i}', s)
    S = {}
    for i, d in zip(search_results['ids'], search_results['documents']):
        for x, y in zip(i, d):
            S[x] = y
    n = len(S.keys())
    n_pairs = round((n**2-n)/2)
    print("Number of possible pairs of selctions", round((n**2-n)/2))
    print(n, n_pairs)

    J = {}
    ct = 0
    K = S.keys()
    for i, p in enumerate(K):
        for j, q in enumerate(K):
            if j > i:
            #    print(f'{p}_{q}')
                J[f'{p}_{q}'] = f"page {p}:\n" + S[p] + f"\n\npage {q}:\n" + S[q]
                ct +=1
    print(len(K), ct)

    singles = bbo.get_embedding([S[k] for k in K])
    
    session_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    MBED = []
    text_pairs = [J[k] for k in J.keys()]
    #p = Pool(int(len(text_pairs)/50))
    #E = p.map(bbo.get_embedding, more_itertools.batched(text_pairs, 50))
    #p.close()

    loop = asyncio.new_event_loop()
    #tasks = [loop.create_task(ops.get_azure_embeddings(p)) for p in paths]
    tasks = [loop.create_task(bbo.async_get_embedding(i, session_id, e)) for i, e in enumerate(more_itertools.batched(text_pairs, 50))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    for e in range(len(tasks)):
        with open(f'/tmp/{session_id}.{e}', 'rb') as f:
            MBED += pickle.load(f)

    combined_embeddings = {}
    combined_text = {}
    for k, s in zip(S.keys(), singles):
        combined_embeddings[k] = s
        combined_text[k] = S[k]
    
    for k, s in zip(J.keys(),  MBED):
        combined_embeddings[k] = s
        combined_text[k] = J[k]



    with open(f'/tmp/{session_id}.mbd', 'wb') as f:
        pickle.dump(combined_embeddings, f)
    with open(f'/tmp/{session_id}.text', 'wb') as f:
        pickle.dump(combined_text, f)

    sidebar = make_sidebar({'Number of possible pairs': n_pairs,
                            'singles': len(S.keys()),
                            'combined': len(J.keys())})

    return wp.optimization_page.format(wp.style, wp.navbar,
                                       sidebar,re.sub("\n", "<br>\n", improved_question), re.sub("\"", "", improved_question), 
                                       'search terms', search_terms, hidden.format('session_id', session_id), wp.script)

@app.route("/")
def welcome():
    return wp.home.format(wp.style, wp.navbar)


















