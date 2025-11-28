# Ticket Assistant — AI Support Agent for a Transport Booking Platform

🧠 Fully local AI assistant that helps end‑users navigate a transport ticketing app.

---

## Overview

Ticket Assistant is an AI-powered conversational agent that guides end-users through:
- Searching for transport routes
- Understanding UI elements and navigation
- Booking flow assistance
- Enforcing strict domain rules (no programming help, no off‑topic content)

Technologies:
- FastAPI backend
- LM Studio local LLM
- FAISS vector search (RAG)
- LangGraph tool-calling
- Spring Boot integration

---

## Features

✔ Local LLM inference via LM Studio  
✔ RAG search using FAISS  
✔ Tools:
- rag_search → reads UI/UX info from frontend_knowledge_base.md
- get_route_options → queries Spring Boot /api/routes/options  
✔ Strict domain rules  
✔ Session-based conversations through a LangGraph state machine  

---

## Project Structure

app/
  api/
    routes.py
    schemas.py
  agent/
    graph.py
  tools/
    rag_tools.py
    route_tools.py
  llm.py
  vectorstore.py
  config.py
  main.py
docs/
faiss_index/
frontend_knowledge_base.md
.env

---

## Installation & Setup

1) Install dependencies:
pip install -r requirements.txt

2) Start LM Studio:
- Load qwen3-vl-4b (recommended)
- Start OpenAI-Compatible Server
- Listening port: 1234

3) Create .env file:
LM_BASE_URL=
LM_API_KEY=
MODEL_NAME=
EMB_MODEL=
DOCS_DIR=./docs
INDEX_DIR=./faiss_index
MD_KNOWLEDGE_BASE=
SPRING_BASE_URL=
USER_AGENT=

4) Start FastAPI:
uvicorn app.main:app --reload --port 8001

---

## API Endpoint

POST /chat

Request:
{
  "message": "How do I search for transport routes?",
  "session_id": "demo123"
}

Response:
{
  "reply": "To search for routes, navigate to the top bar and select 'Find Route'...",
  "session_id": "demo123"
}

