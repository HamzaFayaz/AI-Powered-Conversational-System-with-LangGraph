from typing import Optional, List, Dict, Any
from langgraph.graph import MessagesState

class UnifiedState(MessagesState):
    # Queries
    original_query: Optional[str] = None      # first user query in the thread
    current_query: Optional[str] = None       # latest user query in the thread

    # Agent outputs
    rag_response: Optional[str] = None
    researcher_output: Optional[Dict] = None
    general_output: Optional[Dict] = None

    # Evaluation
    evaluation_result: Optional[Dict] = None

    # Control
    next: Optional[str] = None
    agents_needed: List[str] = []
    query_parts: Optional[List[str]] = None

    # Debug / traces
    retrieved_texts: Optional[Dict[str, Any]] = None
    urls_found: Optional[List[str]] = None
    scraped_content: Optional[Dict[str, str]] = None
    response: Optional[str] = None
    