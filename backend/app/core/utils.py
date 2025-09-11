from typing import List, Optional
from langchain_core.messages import HumanMessage, BaseMessage

def get_last_user_query(messages: List[BaseMessage]) -> Optional[str]:
    """
    Utility: get the latest user message content from history  
    """
    for msg in reversed(messages or []):
        if isinstance(msg, HumanMessage):
            return msg.content
    return None