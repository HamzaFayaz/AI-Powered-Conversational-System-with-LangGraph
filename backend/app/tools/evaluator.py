from langchain_core.tools import tool
from langchain_groq import ChatGroq
from ..models.evaluation import EvaluationResult, QueryPart
from ..core.config import GROQ_API_KEY

@tool
def evaluate_response(query: str, response: str) -> EvaluationResult:
    """
    Evaluate if a response fully answers a query and suggest next steps.
    """
    llm = ChatGroq(model_name="llama-3.3-70b-versatile")
    prompt = f"""
    Evaluate if the response fully answers the latest user query. Provide:
    - A completeness score (0-10).
    - Missing query parts (if any).
    - Whether specialized agents are needed (e.g., researcher for searches).

    Query: {query}
    Response: {response}

    Return a structured response with:
    - completeness_score (0-10)
    - is_complete (true if score >= 8, else false)
    - missing_elements (list of missing parts)
    - query_parts_for_specialized_agents (list of {{part, suggested_agent}} for parts needing researcher)
    """
    try:
        config = {"callbacks": []}
        result = llm.invoke(prompt, config=config).content
        # very forgiving parser (same as your original)
        score = 5
        missing = []
        parts = []
        lines = result.split("\n")
        for line in lines:
            low = line.lower().strip()
            if "score" in low:
                try:
                    score = int(low.split(":")[-1].strip())
                except:
                    pass
            if "missing" in low:
                missing.append(low.split(":")[-1].strip())
            if "research" in low:
                parts.append(QueryPart(part=low.split(":")[-1].strip(), suggested_agent="researcher"))
        is_complete = score >= 8
        if not parts and missing:
            parts = [QueryPart(part=query, suggested_agent="unknown")]
        return EvaluationResult(
            completeness_score=score,
            is_complete=is_complete,
            missing_elements=missing or ["None"],
            query_parts_for_specialized_agents=parts
        )
    except Exception as e:
        return EvaluationResult(
            completeness_score=0,
            is_complete=False,
            missing_elements=[f"Evaluation failed: {str(e)}"],
            query_parts_for_specialized_agents=[QueryPart(part=query, suggested_agent="unknown")]
        )