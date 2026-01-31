# Enterprise Knowledge Co-Pilot

An enterprise-grade GenAI knowledge co-pilot that ingests organizational documents, uses versioned vector indexes for grounded RAG-based Q&A, detects answer regressions across knowledge updates, supports safe rollbacks, and provides full auditability with citations and governance-ready logs.

## Key Capabilities
- Versioned knowledge ingestion
- Grounded Retrieval-Augmented Generation (RAG)
- Strict hallucination control
- Multi-version querying
- Audit-ready answer metadata
- Enterprise-focused architecture

## Tech Stack
- FastAPI
- FAISS
- Sentence Transformers
- Python
- React (planned)
- Cloud deployment (planned)

## Project Structure
- `backend/` – Core APIs, pipelines, vector store
- `frontend/` – UI (Phase 5)
- `artifacts/` – Design decisions, evaluations, governance notes
- `docs/` – API contracts and system documentation

## Status
🚧 Actively under development  
Phase 1: Core RAG with versioned knowledge

## How to Run (Backend)
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
