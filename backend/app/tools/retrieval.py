from langchain_core.tools import tool
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from ..core.config import PINECONE_API_KEY, PINECONE_INDEX

@tool
def retrieval_tool(query_text: str) -> list:
    """
    Retrieve relevant text chunks from a Pinecone vector database based on a query.
    """
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_vector = model.encode(query_text).tolist()
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX)
    response = index.query(vector=query_vector, top_k=5, include_metadata=True)
    # pinecone new SDK returns .matches; but user's earlier dict-like usage worked in their env.
    matches = response.get('matches', []) if isinstance(response, dict) else getattr(response, "matches", [])
    results = [match.get('metadata', {}).get('text', '') for match in matches]
    return results