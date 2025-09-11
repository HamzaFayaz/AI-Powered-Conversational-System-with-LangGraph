# Stage 1: Build the frontend with Node.js 22
FROM node:22-slim AS frontend

WORKDIR /app/frontend

# Copy only package files first for caching
COPY frontend/package*.json ./
RUN npm install

# Copy rest of frontend code and build
COPY frontend/ .
RUN npm run build


# Stage 2: Backend with Python + FastAPI
FROM python:3.11-slim AS backend

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Copy backend requirements
COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY backend/ .

# Copy frontend build into backend (to serve with FastAPI/StaticFiles)
COPY --from=frontend /app/frontend/build ./static

# Expose port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
