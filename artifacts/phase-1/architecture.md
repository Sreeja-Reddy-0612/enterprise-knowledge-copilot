# System Architecture – Phase 1

## High-Level Flow

User
→ FastAPI (/ingest, /query)
→ Ingestion Pipeline
→ Chunking + Embeddings
→ FAISS Vector Store (per knowledge version)
→ Retrieval Pipeline
→ Answer Generation

## Components

### API Layer
- FastAPI
- Swagger-based interaction for development
- Clean separation between ingest and query routes

### Ingestion Pipeline
- PDF parsing
- Text chunking with overlap
- Embedding generation
- Metadata attachment (`knowledge_version`, source)

### Vector Store
- FAISS index per knowledge version
- Stored on disk for persistence
- Enables strict version isolation

### Retrieval
- Semantic similarity search
- Version-filtered retrieval
- Safe empty-context handling

## Architectural Principles
- Modularity
- Explicit versioning
- No hidden global state
- Deployment-ready from Phase 1
