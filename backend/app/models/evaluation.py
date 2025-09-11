from typing import List, Literal
from pydantic import BaseModel, Field

class QueryPart(BaseModel):
    part: str = Field(description="Part of the query needing further processing")
    suggested_agent: Literal["researcher", "unknown"] = Field(description="Suggested agent to handle this part")

class EvaluationResult(BaseModel):
    completeness_score: int = Field(ge=0, le=10, description="Score from 0-10 for response completeness")
    is_complete: bool = Field(description="Whether the response fully answers the query")
    missing_elements: List[str] = Field(description="List of missing or inadequately addressed query parts")
    query_parts_for_specialized_agents: List[QueryPart] = Field(description="Query parts needing specialized agents")