search_term_prompt = """I'm going to give you a query. Your job is to write search expressions to help me search for text that would be similar to the answer.
The search expression should be descriptive so that it finds the right text. Write no more than 5 search expressions and put them in a list like this example:
### EXAMPLE QUERY ###
What is the best French Food?

### YOUR ANSWER ###
['French food', 'French Restaurants', 'Popular French lunches']

Return only the list of search terms and no other text. Do not explain or introduce your answer.

### QUERY ###
"""

improve_query = """You are a prompt engineer. Someone has provided a query for a language model. Rewrite the query and add details. Try to guide the language model to help it know how to do a good job of answering the question.
Only provide the rewritten query. Do not introduce or eplain your answer or provide any other text.

### QUERY ###
"""

relevance_prompt = """I'm going to give you a query and some text. Your job is to rate the relevance of the reference to the query. 
Consider how complete the available text is and how detailed it is in your determination.
Completeness and detail are not only requirement for relevance but are important.
Choose your answer from the following list:
"critical relevance" "very relevant", "very relevant", "somewhat relevant", "mostly irrelevant", "completely irrelevant", "distracting"

Here is rubrik to explain how to provide an answer:
- "critical relevance": If the information in the text is essential for answering the question and gives all necessary information.
- "very relevant": The text helps to answer the question but is missing a little bit.
- "somewhat relevant": The text provides limited, helpful information.
- "mostly irrelevant": The text is barely related to the query.
- "completely irrelevant": The text has nothing to do with the query. It is unrelated.
- "distracting": The text actually interferes with the ability to answer the question. It seems relevant but is actually misleading.

You might be given two passages. If so, your answer should account for both passages together. Do not penalize if one is relevant and the other is not but give extra bonus if the combination helps you to provide a better answer.
Do not penalize if there is extraneous information. Penalize slightly if the information is outdated but would have been relevant otherwise.

Do not introduce your answer. Do not provide any other labels or other text. Only give the JSON answer with the keys "rationale" and "relevance" in that order.

Put your rationale and answer in JSON format. Here is an example:
### EXAMPLE QUERY ###
When did the romantic period begin?

### EXAMPLE REFERENCES ###
There once was man from Nantucket. He kept his money in a bucket

### EXAMPLE OF YOUR ANSWER ###
{{"rationale": "The reference does not talk about the Romantic period at all. However, it is a limerick and that may have been somewhat popular in the romantic era. The text does not contain information that would be helpful in answer the query.",
 "relevance": "mostly irrelevant"}}

### QUERY ###
{}

### TEXT ###
{}
"""


rag = """I'm going to give you a question with some references. Try to answer the question. If you use the references, indicate that you have used them. 
If you cannot answer the question from the references of if the references are only partially helpful, indicate that as well. Do not speculate beyond what is contained in the references.

#### QUESTION ###
{}

### REFERENCES ###
{}
"""