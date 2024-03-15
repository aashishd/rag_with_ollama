from fastapi import FastAPI
from llm_interaction import LocalLLM
# The file where NeuralSearcher is stored
from search_api import NeuralSearcher

app = FastAPI()

# Create a neural searcher instance
neural_searcher = NeuralSearcher(collection_name="startups")

# create the local llm
local_llm = LocalLLM()


def build_context(payloads):
    descriptions = "\n".join([payload["description"] for payload in payloads])
    return f"Here's the descrition of some similar startups I found:\n{descriptions}"
                             

@app.get("/api/search")
async def search_startup(q: str):
    llmcontext = neural_searcher.search(text=q)
    response = local_llm.chat(query=q, context=llmcontext)
    return {"result": response, 'context':llmcontext}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)