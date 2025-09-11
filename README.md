# Agentic_Chatbot
<div align="center">

![LangGraph](https://img.shields.io/badge/LangGraph-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![LangSmith](https://img.shields.io/badge/LangSmith-00C4CC?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00C4CC?style=for-the-badge&logo=python&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![Node.js 18+](https://img.shields.io/badge/node.js-18+-green.svg?style=for-the-badge)](https://nodejs.org/)

</div>

## 📋 About This Project

An advanced AI-powered conversational system built with modular architecture for scalability, maintainability, and clarity. The project leverages LLMs orchestrated through LangGraph for structured reasoning, while maintaining a professional ingestion workflow to handle document uploads and populate a vector database for accurate retrieval.  

### What Makes It Special:
- 🧠 **Agent-Centric Design**: Agents are fully separated from prompts, nodes, and graph logic for clean reasoning flow.  
- 📂 **Structured Ingestion**: Dedicated ingestion pipeline for loading, chunking, and embedding documents into the vector database.  
- 🔎 **Powerful Retrieval**: Optimized vector search ensures precise context recall for user queries.  
- 🪄 **Modular Workflow**: Clear split between core logic (agents, nodes, graph) and shared helpers (utils, config) for easy scaling.  
- 📊 **Transparent Orchestration**: LangGraph-based graph definition provides visibility and control over multi-step reasoning.  
- ⚡ **Seamless Integration**: Built-in support for FAISS/Pinecone and other vector DBs for flexible deployment.  

---

## 📊 **System Overview**
<img width="492" height="432" alt="System_Architecture" src="https://github.com/user-attachments/assets/129a811b-af7d-4352-bfa9-ff8e27e5504a" />

---
## 🚀 Key Features

### Core Functionality
- 🧠 **AI-Powered Agents**: Modular agents designed for reasoning, tool use, and clean separation from prompts and graph logic.  
- 📂 **Document Ingestion & Management**: Upload, split, and embed documents into FAISS/Pinecone vector databases.  
- 🔎 **RAG (Retrieval-Augmented Generation)**: Context-aware query responses using vector embeddings for precise retrieval.  
- 🪄 **LangGraph Orchestration**: Multi-stage conversational workflow built with LangGraph for structured reasoning.  
- ⚡ **Real-time Query Handling**: Asynchronous FastAPI endpoints for fast, scalable request processing.  
- 📊 **Transparent Execution**: Workflow steps traceable through LangGraph’s state graph definition.  
- 🔌 **Seamless Integration**: Built-in support for FAISS and Pinecone for flexible storage/retrieval.  

### Frontend Features
- 🎨 **Modern UI**: Built with React, Tailwind CSS, and Framer Motion for a sleek, interactive design.  
- 📱 **Responsive Design**: Mobile-friendly interface with adaptive layouts.  
- 📂 **File Upload**: Drag-and-drop document upload with progress indicators.  
- 💬 **Chat Interface**: Conversational chatbot UI with context-aware responses.  
- 🔄 **Live Updates**: Real-time chat flow and retrieval tracking.  
- 🧩 **API Integration**: Direct connection to FastAPI backend endpoints.  

### Backend Features
- ⚡ **FastAPI Backend**: High-performance Python backend serving as the core API layer.  
- 🪄 **LangGraph Workflow Engine**: Node-based orchestration of agent workflows.  
- 📂 **Vector Database**: FAISS/Pinecone support for document storage and retrieval.  
- 🧠 **Agents & Tools**: Clear separation of agents, prompts, nodes, and ingestion pipelines.  
- 🔄 **Asynchronous Processing**: Handles multiple concurrent requests with async FastAPI.  
- 📜 **API Documentation**: Auto-generated OpenAPI docs available at `http://localhost:8000/docs`.  
- 🐳 **Docker Support**: Ready for containerized deployment and scaling.  

---
