from typing import Literal
from langgraph.types import Command
from langgraph.graph import END
from langchain_core.messages import AIMessage
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from .state import UnifiedState
from ..agents.research_agent import create_research_agent
from ..agents.rag_agent import create_rag_agent
from ..agents.general_agent import create_general_agent
from ..tools.evaluator import evaluate_response
from ..core.utils import get_last_user_query

# Initialize agents
research_agent = create_research_agent()
rag_agent = create_rag_agent()
general_knowledge_agent = create_general_agent()

def rag_node(state: UnifiedState) -> Command[Literal["supervisor"]]:
    result = rag_agent.invoke({"messages": state["messages"]})
    rag_response = result["messages"][-1].content
    return Command(
        update={
            "messages": [AIMessage(content=rag_response, name="Rag_agent")],
            "retrieved_texts": result,
            "rag_response": rag_response
        },
        goto="supervisor",
    )

def research_node(state: UnifiedState) -> Command[Literal["final_response"]]:
    result = research_agent.invoke({"messages": state["messages"]})
    scraped_content = result["messages"][-1].content
    researcher_output = {
        "search_query": state.get("current_query"),
        "scraped_content": {"content": scraped_content},
    }
    return Command(
        update={
            "messages":  [AIMessage(content=scraped_content, name="Researcher")],
            "researcher_output": researcher_output
        },
        goto="final_response",
    )

def general_node(state: UnifiedState) -> Command[Literal["final_response"]]:
    result = general_knowledge_agent.invoke({"messages": state["messages"]})
    general_response = result["messages"][-1].content
    return Command(
        update={
            "messages":  [AIMessage(content=general_response, name="General_agent")],
            "general_output": {"response": general_response, "query": state.get("current_query")}
        },
        goto="final_response",
    )

def supervisor_node(state: UnifiedState) -> Command[Literal["rag_agent", "researcher", "general_agent", "final_response"]]:
    # set original + current queries from conversation
    if state["messages"]:
        if not state.get("original_query"):
            # first user message in the thread
            
            first_user = next((m for m in state["messages"] if isinstance(m, HumanMessage)), None)
            if first_user:
                state["original_query"] = first_user.content
        # latest user message in the thread
        state["current_query"] = get_last_user_query(state["messages"])

    # If we haven't run RAG yet in this turn, try it first
    if not state.get("rag_response"):
        return Command(update={"messages": state["messages"]}, goto="rag_agent")

    # Evaluate RAG response against the LATEST user message (not the original)
    config = {"callbacks": []}
    evaluation = evaluate_response.invoke(
        {"query": state.get("current_query", state.get("original_query", "")),
         "response": state["rag_response"]},
        config=config
    )
    state["evaluation_result"] = evaluation.model_dump()

    # If RAG is complete, finish
    if evaluation.is_complete:
        return Command(update=state, goto="final_response")

    # Route based on suggestions
    suggested_agents = [part.suggested_agent for part in evaluation.query_parts_for_specialized_agents]

    if "researcher" in suggested_agents:
        # NOTE: do NOT truncate messages; pass full history
        return Command(update=state, goto="researcher")

    # Unknown or incomplete → general agent for explanation/clarification
    if "unknown" in suggested_agents or not evaluation.is_complete:
        return Command(update=state, goto="general_agent")

    # Fallback
    return Command(update=state, goto="final_response")

def final_response_node(state: UnifiedState) -> Command[Literal[END]]:
    final_response_llm = ChatGroq(model_name="llama-3.3-70b-versatile")
    rag_content = state.get("rag_response", "No RAG output")
    researcher_content = state.get("researcher_output", {}).get("scraped_content", {}).get("content", "No researcher output")
    general_content = state.get("general_output", {}).get("response", "No general agent output")

    evaluation = state.get("evaluation_result", {})
    is_complete = evaluation.get("is_complete", False)
    missing_elements = evaluation.get("missing_elements", ["None"])

    final_response_prompt = f"""
    You are a final response generator. Produce a clear, concise answer to the user's latest query by considering the FULL conversation history and integrating the agent outputs.

    Latest User Query: {state.get("current_query", state.get("original_query", ""))}
    RAG Agent Output: {rag_content}
    Researcher Output: {researcher_content}
    General Agent Output: {general_content}
    Evaluation: The RAG response {'fully answers' if is_complete else 'does not fully answer'} the latest query.
    Missing Elements (if any): {missing_elements}

    Instructions:
    - do not qoute the  finale response with signle or double , just a clean text if heading is requred or can made the made that
    - Do NOT say things like "Based on the provided data..."; just answer directly.
    - If Researcher Output has concrete, current facts, prioritize them.
    - Use General Agent Output for conceptual explanations.
    - Use RAG Output to supplement only if needed.
    - If overall incomplete, acknowledge and suggest what specific info would help.
    - Keep it concise and well-structured.
    """

    response = final_response_llm.invoke(final_response_prompt).content
    return Command(
        update={"messages":  [AIMessage(content=response, name="final_response")]},
        goto=END,
    )