from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import MemorySaver
from .state import UnifiedState
from .nodes import supervisor_node, research_node, rag_node, general_node, final_response_node

def create_graph():
    memory = MemorySaver()
    builder = StateGraph(UnifiedState)
    builder.add_edge(START, "supervisor")
    builder.add_node("supervisor", supervisor_node)
    builder.add_node("researcher", research_node)
    builder.add_node("rag_agent", rag_node)
    builder.add_node("general_agent", general_node)
    builder.add_node("final_response", final_response_node)
    return builder.compile(checkpointer=memory)