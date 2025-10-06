import openai
import re
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import WhiteKernel, Matern, DotProduct
from scipy.stats import ecdf, lognorm
import numpy as np
import requests
import json
import random

def x_relevance(answer):
    try:
        j = eval(re.sub('json', '', re.sub('`', '', answer)))
        if j['relevance'] == "critical relevance":
            score = 1
        elif j['relevance'] == "very relevant":
            score = .83
        elif j['relevance'] == "somewhat relevant":
            score = .65
        elif j['relevance'] == "mostly irrelevant":
            score = .5
        elif j['relevance'] == "completely irrelevant":
            score = .33
        elif j['relevance'] == "distracting":
            score = .16
        return score
    except Exception as e:
        print(e)
        print(answer)
        return -1

def get_embedding(text):
    embed_model_name = "embed-v-4-0"

    client = EmbeddingsClient(
        endpoint=os.environ['EMBED_ENDPOINT'],
        credential=AzureKeyCredential(os.environ['EMBED_KEY'])
    )
    response = client.embed(
        input = text,
        model=embed_model_name
    )
    
    print(response.usage)
    
    return [e.embedding for e in response.data]
    


class best_batch_finder:
    def __init__(self, n_batches, batch_size):
        self.n_batches = n_batches
        self.batch_size = batch_size
    def fit(self, scored_answers, embeddings):


        self.best = -1000
        s = [-1]
        for s in scored_answers.keys():
            if scored_answers[s] > self.best:
                print(self.best, scored_answers[s])
                self.best = scored_answers[s]
                self.best_prompt_id = s

        Q = [scored_answers[s] for s in scored_answers.keys()]
        scored_embeddings = [embeddings[s] for s in scored_answers.keys()]
        unscored_embeddings = []
        index2id = {}
        ct = 0
        for s in embeddings.keys():
            if s not in scored_answers.keys():
                unscored_embeddings.append(embeddings[s])
                index2id[ct] = s
                ct += 1
        
        self.gpr = GaussianProcessRegressor(kernel = Matern() + WhiteKernel())
        scores_ecdf = ecdf(Q)
        transformed_scores = np.log(lognorm.ppf(scores_ecdf.cdf.evaluate(Q) * .999 + .0005, 1))
        self.gpr.fit(scored_embeddings, transformed_scores)
        self.y_best = max(transformed_scores)
        self.mu, self.sigma = self.gpr.predict(unscored_embeddings, return_cov=True)
        return index2id, unscored_embeddings
        
    def create_batches(self, rollout_embeddings):
        self.batch_mu = []
        self.batch_sigma = []
    
        batches = []
        self.batch_idx = []
        n_to_choose_from = len(rollout_embeddings)
        for z in range(self.n_batches):
            batch = []
            for x in range(self.batch_size):
                rx = random.randint(0, n_to_choose_from-1)
                while rx in batch:
                    rx = random.randint(0, n_to_choose_from-1)
                batch.append(rx)
    
            self.batch_idx.append(batch)
            m, s = self.gpr.predict([rollout_embeddings[i] for i in batch], return_cov=True)
            self.batch_mu.append(','.join([str(x) for x in m]))
            sigma = []
            for x in s:
                sigma.append(','.join([str(y) for y in x]))
            self.batch_sigma.append(';'.join(sigma))
        
        
    def get_best_batch(self, gpu=False):
        try:
            #url = 'https://boaz.onrender.com/qei?y_best=.02&n=' + str(n)
            if gpu:
                url = f'http://34.130.49.1:5000/gpu_qei?y_best={self.y_best}&n={self.batch_size}'
            else:
                url = f'https://boaz.onrender.com/qei?y_best={self.y_best}&n={self.batch_size}'
            data = {'k': ';'.join(self.batch_mu),
                    'sigma': '|'.join(self.batch_sigma)}
            response = requests.post(url, json.dumps(data))
            boaz = eval(response.content.decode('utf-8'))
        except Exception as e:
            print('Bayesian Issues:', e)
            #print(batch_sigma)
            return random.randint(0, len(self.batch_mu))
        fboaz = [float(x) for x in boaz['scores'].split(',')]
        best = -1
        for i, mx in enumerate(fboaz):
            if mx > best:
                best = float(mx)
                best_idx = i
        return best_idx
            


def call_gpt(p):
    messages = [{"role": "system", "content": p['system'],
                 "role": "user", "content": p['user']}]
    azure_client = openai.AzureOpenAI(
            api_key=os.environ['AZURE_OPENAI_KEY'],
            api_version="2024-10-21",
            azure_endpoint = os.environ['AZURE_ENDPOINT']
            )
    response = azure_client.chat.completions.create(
            model='gpt-4o',
            messages = messages
            )
    return response.choices[0].message.content
    