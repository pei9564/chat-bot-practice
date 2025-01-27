import os
from langchain_community.chat_models.ollama import ChatOllama
from langchain_core.messages import HumanMessage

def get_ollama_llm():
    model_name = os.environ.get("OLLAMA_MODEL", "llama3.2:1b")
    ollama_base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
    return ChatOllama(model=model_name, base_url=ollama_base_url)

def chat(input):
    llm = get_ollama_llm()
    result = llm.invoke([HumanMessage(content=input)])
    return result.content