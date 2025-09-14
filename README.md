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

---

## 📋 **About This Project**

An advanced **AI-powered conversational system** built with modular architecture for scalability, maintainability, and clarity. The project leverages **LLMs orchestrated through LangGraph** for structured reasoning, while maintaining a professional ingestion workflow to handle document uploads and populate a vector database for accurate retrieval.  

### **What Makes It Special:**
- 🧠 **Agent-Centric Design**: Agents are fully separated from prompts, nodes, and graph logic for clean reasoning flow.  
- 📂 **Structured Ingestion**: Dedicated ingestion pipeline for loading, chunking, and embedding documents into the vector database.  
- 🔎 **Powerful Retrieval**: Optimized vector search ensures precise context recall for user queries.  
- 🪄 **Modular Workflow**: Clear split between core logic (agents, nodes, graph) and shared helpers (utils, config) for easy scaling.  
- 📊 **Transparent Orchestration**: LangGraph-based graph definition provides visibility and control over multi-step reasoning.  
- ⚡ **Seamless Integration**: Built-in support for FAISS/Pinecone and other vector DBs for flexible deployment.  
- 🐳 **Unified Dockerization**: Frontend (React) and Backend (FastAPI) fully containerized and deployed together.  
- 🔄 **Automated CI/CD Pipeline**: Continuous integration and delivery for seamless testing, building, and deployment.  
- ☁️ **Cloud Ready**: Supports deployment on **AWS EC2** with container images stored in **Amazon ECR** for production scalability.  
- 💻 **Local Friendly**: Runs smoothly on local machines or Codespaces with Docker Compose if AWS is not required.  

---

## 📸 **Demo & Screenshots**

Here are some snapshots that highlight the system in action:  

### 💬 Chatbot Demo  
Showcasing real-time interaction with the AI-powered conversational system.  
<img width="650" height="961" alt="chatbot_1" src="https://github.com/user-attachments/assets/8e06bc06-c1ff-4440-88b0-cfd1d6e33434" />
<img width="650" height="713" alt="chatbot_2" src="https://github.com/user-attachments/assets/1866612a-9ccb-4fcf-9e97-3473d6c67832" />



---

### ☁️ AWS EC2 Deployment  
CI/CD pipeline success message from the **EC2 instance terminal**.  

<img width="1527" height="696" alt="Runner aws" src="https://github.com/user-attachments/assets/00d84f1c-ef9d-405a-b451-75bcd6ac779b" />

---

### 🔄 GitHub Actions Workflow  
Successful **workflow run** demonstrating automated CI/CD.  

<img width="1746" height="712" alt="cicd running" src="https://github.com/user-attachments/assets/fd462323-ecc1-4eab-ae38-054742a84a05" />


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
## 🏗️ **System Architecture**

```text
┌─────────────────┐    ┌─────────────────┐    ┌───────────────────────┐
│   Frontend      │    │   Backend       │    │     AI Services       │
│   (React)       │◄──►│ (FastAPI +      │◄──►│   (LangGraph + LLMs)  │
│                 │    │   LangGraph)    │    │                       │
│ • Chatbot UI    │    │ • API Gateway   │    │ • Agents & Graph Flow │
│ • File Upload   │    │ • Ingestion     │    │ • Retrieval + RAG     │
│ • Live Updates  │    │ • Vector Store  │    │ • Document Embedding  │
│ • Reports       │    │ • CI/CD Hooks   │    │ • AWS EC2 + ECR       │
└─────────────────┘    └─────────────────┘    └───────────────────────┘

```

---

## 📁 **Project Structure**

The project follows a clean and modular structure for clarity and scalability.  

```text
chatbot-project/
├── backend/                     # FastAPI backend
│   ├── app/
│   │   ├── agents/              # AI agents
│   │   ├── api/                 # API routes
│   │   ├── core/                # Core logic (entrypoints)
│   │   ├── graph/               # LangGraph workflows
│   │   ├── ingestion/           # Document ingestion pipeline
│   │   ├── models/              # ML/LLM models
│   │   ├── prompts/             # LLM prompts
│   │   ├── tools/               # Helper tools
│   │   ├── __init__.py          # Package init
│   │   └── main.py              # FastAPI app entrypoint
│   ├── run.py                   # Run script
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Environment variables
│   └── Dockerfile               # Backend Docker configuration
│
├── frontend/                    # React frontend
│   ├── public/                  # Static assets
│   ├── src/                     # Frontend source code
│   │   ├── components/          # React components
│   │   ├── services/            # API services
│   │   └── utils/               # Frontend utilities
│   ├── package.json             # Node.js dependencies
│   ├── package-lock.json        # Dependency lock file
│   └── tailwind.config.js       # Tailwind CSS config
│
├── docker-compose.yml           # Compose for fullstack deployment
├── .dockerignore                # Files ignored by Docker
└── README.md                    # Project documentation
```

## 🛠️ Technology Stack  

### Backend  
- **FastAPI**: Modern Python web framework for building APIs  
- **Uvicorn**: Lightning-fast ASGI server for running FastAPI  
- **Docker**: Containerization for consistent deployments  
- **AWS EC2**: Hosting the backend on a scalable cloud VM  
- **AWS ECR** *(optional)*: Private container registry for storing Docker images  

### Frontend  
- **React 18**: UI framework for building responsive frontend  
- **Tailwind CSS**: Utility-first CSS framework for styling  
- **Framer Motion**: Animation library for smooth UI interactions  
- **React Hook Form**: Form handling and validation  
- **React Dropzone**: File upload functionality  
- **Headless UI**: Accessible, unstyled components  

### AI/ML  
- **Sentence Transformers**: Text embeddings for semantic similarity  
- **FAISS**: Vector similarity search for efficient retrieval  
- **LangChain**: LLM orchestration and RAG pipeline management  

### DevOps / CI/CD  
- **GitHub Actions**: Automating CI/CD workflows  
- **Docker**: Containerized builds for portability  
- **AWS EC2**: Deployment target for CI/CD pipeline  
---

## 🚀 Quick Start

Get the project running locally in just a few steps:  

```bash
# 1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2️⃣ Backend Setup (FastAPI)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

# Run the backend server
python run.py
# 👉 Backend available at http://127.0.0.1:8000

# 3️⃣ Frontend Setup (React)
cd frontend
npm install
npm start
# 👉 Frontend available at http://localhost:3000

# 4️⃣ Run with Docker (Optional)
# From the project root
docker build -t agentic-chatbot:latest .
docker run -d -p 8000:8000 --env-file backend/.env agentic-chatbot:latest

# 5️⃣ Deploy to AWS EC2 (Optional)
# Copy files to EC2 instance
scp -r . ubuntu@your-ec2-ip:/home/ubuntu/agentic-chatbot

# SSH into EC2
ssh ubuntu@your-ec2-ip

# Inside EC2 instance
cd agentic-chatbot
docker build -t agentic-chatbot:latest .
docker run -d -p 8000:8000 --env-file backend/.env agentic-chatbot:latest
```

