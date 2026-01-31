# Versioned Vector Database Design

## Overview
Phase 2 introduces a **versioned vector database** architecture that isolates
knowledge across multiple deployments.

Each knowledge version maintains its own:
- FAISS index
- Metadata store
- Ingestion lifecycle

This prevents cross-document contamination and enables safe rollouts.

---

## Storage Layout

backend/vectorstore/
├── v1.0.0.index
├── v1.0.0.index.meta.npy
├── resume.index
├── resume.index.meta.npy

---

## Ingestion Flow
1. User uploads document with `knowledge_version`
2. Document is chunked
3. Chunks are embedded
4. Vectors stored in FAISS index named after version
5. Metadata stored alongside index

---

## Query Flow
1. Active version is fetched
2. Query embedding generated
3. FAISS search executed only on active index
4. Top-K chunks returned
5. Answer generated from retrieved context

---

## Guarantees
- Queries never access inactive versions
- Old versions remain intact
- Multiple documents can coexist safely

---

## Why This Matters
This design mirrors **enterprise knowledge deployment** where:
- Models evolve
- Knowledge changes
- Rollbacks must be safe

