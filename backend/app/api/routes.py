from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
import tempfile
import os
from langchain_core.messages import HumanMessage

from ..graph.builder import create_graph
from ..ingestion.loaders import load_pdf, load_text_file
from ..ingestion.uploader import store_text_in_pinecone

router = APIRouter()

# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str
    chatbot_id: str
    thread_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    thread_id: str

class UploadResponse(BaseModel):
    chatbot_id: str
    message: str
    filename: str

# Initialize the graph once
graph = create_graph()

@router.post("/upload-file", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    """
    Upload and process a file for the chatbot.
    Supports PDF and text files.
    """
    try:
        # Generate unique chatbot ID
        chatbot_id = str(uuid4())
        
        # Check file type
        if not file.filename:
            raise HTTPException(status_code=400, detail="No filename provided")
        
        file_extension = file.filename.lower().split('.')[-1]
        
        if file_extension not in ['pdf', 'txt']:
            raise HTTPException(
                status_code=400, 
                detail="Unsupported file type. Only PDF and TXT files are allowed."
            )
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            # Process file based on type
            if file_extension == 'pdf':
                text_content = load_pdf(temp_file_path)
            else:  # txt
                text_content = load_text_file(temp_file_path)
            
            # Store in Pinecone
            store_text_in_pinecone(text_content)
            
            return UploadResponse(
                chatbot_id=chatbot_id,
                message="File uploaded and processed successfully",
                filename=file.filename
            )
            
        finally:
            # Clean up temporary file
            os.unlink(temp_file_path)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message to the chatbot and get a response.
    """
    try:
        # Use provided thread_id or create new one
        thread_id = request.thread_id or str(uuid4())
        
        # Configure the graph with thread ID
        config = {"configurable": {"thread_id": thread_id}}
        
        # Create user message
        user_message = HumanMessage(content=request.message)
        
        # Run the graph
        result = graph.invoke({"messages": [user_message]}, config=config)
        
        # Extract the final response
        bot_response = result["messages"][-1].content
        
        return ChatResponse(
            response=bot_response,
            thread_id=thread_id
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@router.get("/chatbot/{chatbot_id}")
async def get_chatbot_info(chatbot_id: str):
    """
    Get information about a specific chatbot.
    """
    return {
        "chatbot_id": chatbot_id,
        "status": "active",
        "message": "Chatbot is ready for conversation"
    }

