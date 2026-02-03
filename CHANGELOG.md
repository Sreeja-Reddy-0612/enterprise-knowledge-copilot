# Changelog

## v0.4.1 – Phase 5.2 (Development)
### Added
- Runtime configuration validation at application startup
- Centralized typed settings management
- Explicit environment sanity checks (paths, models, version files)
- Startup logging for operational visibility

### Improved
- Application startup reliability
- Failure transparency for misconfiguration
- Production readiness and maintainability
- Safety against invalid runtime state

---

## v0.4.0 – Phase 4 Completed
### Added
- Frontend application (Vite + React)
- Knowledge upload UI with version tagging
- Active knowledge version display
- Rollback control from UI
- Query interface with navigation flow
- Display of answer, trace_id, and knowledge versions
- Frontend–backend API orchestration
- CORS-safe integration

### Improved
- End-to-end usability from ingestion → query → rollback
- Debugging and observability via trace_id visibility in UI

---

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
