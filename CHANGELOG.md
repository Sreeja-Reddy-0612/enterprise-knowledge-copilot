# Changelog

## v0.3.0 – Phase 3 Completed
### Added
- Multi-version knowledge lifecycle (DRAFT / ACTIVE / DEPRECATED)
- Runtime version rollback API
- Query-time version override support
- Multi-version retrieval with global ranking
- End-to-end observability with trace_id
- Structured logging across ingestion, retrieval, query, and rollback
- Audit logs for version transitions

### Fixed
- Silent version override failures
- Retrieval leakage across inactive versions
- Missing trace propagation across pipelines

---

## v0.2.0 – Phase 2 Completed
### Added
- Versioned document ingestion pipeline
- Persistent FAISS vector index per knowledge version
- Semantic chunk retrieval using SentenceTransformers
- Active version enforcement during query execution
- Retrieval debugging (distances, indices, chunk inspection)
- Support for multiple document types under same version

### Fixed
- Empty retrieval issues due to version mismatch
- FAISS index reload inconsistencies
- Incorrect query execution on inactive versions

---

## v0.1.0 – Phase 1 Completed
### Added
- Core RAG pipeline
- Document ingestion with version tagging
- FAISS-based vector store
- Version-aware retrieval
- Grounded answer generation with refusal

---

## v0.0.1
### Added
- Project skeleton
- Repository structure
- Initial configuration
