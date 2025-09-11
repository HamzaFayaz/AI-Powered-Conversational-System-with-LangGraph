from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from ..prompts.rag_prompt import RAG_PROMPT
from ..tools.retrieval import retrieval_tool

def create_rag_agent():
    llm = ChatGroq(model_name="llama-3.3-70b-versatile")
    return create_react_agent(llm, tools=[retrieval_tool], prompt=RAG_PROMPT)