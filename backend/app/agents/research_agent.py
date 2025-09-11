from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from ..prompts.research_prompt import RESEARCH_PROMPT
from ..tools.scraper import scrape_and_clean_url
from ..core.config import TAVILY_API_KEY

def create_research_agent():
    llm = ChatGroq(model_name="llama-3.3-70b-versatile")
    tavily_tool = TavilySearchResults(max_results=5, tavily_api_key=TAVILY_API_KEY)
    return create_react_agent(llm, tools=[tavily_tool, scrape_and_clean_url], prompt=RESEARCH_PROMPT)