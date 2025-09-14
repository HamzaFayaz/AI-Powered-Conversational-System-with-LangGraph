from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router as api_router
from .api.healthcheck import router as health_router
from fastapi.staticfiles import StaticFiles

# Serve React build (so frontend available at "/")


app = FastAPI(
    title="AI Chatbot API",
    description="FastAPI backend for AI chatbot with file upload and RAG capabilities",
    version="1.0.0"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(api_router, prefix="/api", tags=["chat"])

@app.get("/checking")
async def root():
    return {"message": "AI Chatbot API is running"}


app.mount("/", StaticFiles(directory="static", html=True), name="frontend")


