# Bayesian Reranker
This demo shows how to scale an LLM reranker for cross-hop reasoning using batch Bayesian optimization.

### Steps
1. **Embeddings** - In this example, we use a Mini-Wiki corpus and convert it to a vector db. (This is already included)
2. **Create Search Terms** - Convert the question into some search expressions to facilitate searching the vector db. The answer usually doesn't look like the question so, use an LLM to come up with search terms.
3. **Improve the question** - Once you have a question that is asking for very detailed answers, it's easier to rate the text as relevant or not.
4. **Define Search Space** - We are going to search the results and also evaluate the relevance pairwise. The purpose of this is to enable cross hop reasoning. This causes the search space to increase. This can be done for larger groups of retreivals.
5. **Evaluate Initial Random Sample** - Select some random samples and evaluate pointwise. This can also be done pairwise.
6. **Bayesian Optimization** - Use the results to create Quante Carlo's optimal batch calculator: this is the optimal retreivals to evaluate in parallel.
7. **Evaluate Next Retreivals** - Evaluate retreivals and answer iteratively, using the Bayesian optimizater until the answer is satsifactory.


## Build your own
- This comes with a server and you can make your own changes. You will need credentials (of course) for your AI backend.
- For the massively parallel part you will need the [Bayesian batch finder.](https://rapidapi.com/info-FLGers_gH/api/batch-bayesian-optimization)
- contact me with questions info@quantecarlo.com

