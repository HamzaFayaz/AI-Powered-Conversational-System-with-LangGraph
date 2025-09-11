from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from ..prompts.general_prompt import GENERAL_PROMPT

def create_general_agent():
    llm = ChatGroq(model_name="llama-3.3-70b-versatile")
    return create_react_agent(llm, tools=[], prompt=GENERAL_PROMPT)