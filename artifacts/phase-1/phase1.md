# Phase 1 – Core RAG with Versioned Knowledge

## Objective
Build a production-grade Retrieval-Augmented Generation (RAG) foundation that ingests enterprise documents, converts them into embeddings, and enables grounded question answering with explicit knowledge versioning.

## What Was Implemented
- FastAPI backend with modular API structure
- `/ingest` endpoint for PDF document upload
- Text extraction, chunking, and embedding using Sentence Transformers
- FAISS vector store for semantic retrieval
- Metadata tagging of every chunk with `knowledge_version`
- `/query` endpoint accepting question + knowledge_version
- Strict refusal behavior when no relevant context exists

## Key Design Choices
- Knowledge versions are treated as **metadata**, not logic
- Vector indexes are isolated per knowledge version
- Absolute imports (`backend.*`) enforced for deployment safety

## Outcome
The system now supports version-aware RAG, forming the foundation for multi-version comparison, rollback, and regression detection in later phases.
