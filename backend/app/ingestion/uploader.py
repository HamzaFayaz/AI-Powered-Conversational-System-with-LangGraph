from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from .splitter import split_text
from ..core.config import PINECONE_API_KEY, PINECONE_INDEX

def store_text_in_pinecone(text: str, chunk_size: int = 200):
    """
    Store text data in Pinecone after converting to embeddings.     
    Parameters:
    - text: The text to store
    - chunk_size: Size of text chunks to split into
    """
    # Split text into chunks
    chunks = split_text(text, chunk_size)
    
    # Initialize the embedding model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    # Generate embeddings for each chunk
    embeddings = model.encode(chunks)
    
    # Initialize Pinecone
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX)
    
    # Prepare vectors for upsert
    vectors = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vectors.append({
            "id": f"chunk_{i}",
            "values": embedding.tolist(),
            "metadata": {"text": chunk}
        })
    
    # Upsert to Pinecone
    index.upsert(vectors=vectors)
    print(f"Stored {len(chunks)} text chunks in Pinecone")