from langchain_community.llms import Ollama

LLM_HOST = "http://host.docker.internal:11434"

class LocalLLM:
    def __init__(self) -> None:
        self.llm = Ollama(model="llama2", base_url=LLM_HOST)
    
    def chat(self, query: str, context: str) -> str:
        qwithcontext = f"Given the following context '{context}' generate a creative response for the following question '{query}'"
        return self.llm.invoke(qwithcontext)
        