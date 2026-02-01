# Phase 3 – Regression Detection Strategy

Phase 3 introduces **version-aware regressions**.

## Regression Risks

1. Query returning results from deprecated versions
2. Rollback not updating active retrieval scope
3. Trace ID mismatch across services
4. Silent failures during ingestion

## Detection Mechanisms

- Structured logs with trace_id
- Version-tagged retrieval logs
- Manual verification using:
  - /version/active
  - /version/rollback
  - Query override payloads

## Regression Testing (Manual)
- Ingest same document under multiple versions
- Switch active version
- Verify source attribution changes

Automated regression testing is deferred to Phase 4.
