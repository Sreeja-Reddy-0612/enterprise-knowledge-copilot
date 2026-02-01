# Phase 3 – Evaluation Metrics

Phase 3 focuses on **system-level correctness**, not model accuracy.

## Metrics Tracked

### 1. Retrieval Correctness
- Retrieved chunks must belong only to:
  - Active versions
  - Or explicitly overridden versions
- No leakage across deprecated versions

### 2. Version Consistency
- Queries without override must respect `active_version`
- Rollback must immediately affect retrieval behavior

### 3. Trace Integrity
- Every request must generate a unique `trace_id`
- The same `trace_id` must appear in:
  - API logs
  - Retrieval logs
  - Rollback logs

### 4. Operational Safety
- Missing vector indexes should not crash queries
- Empty retrieval must return safe refusal responses

## Non-goals (Out of Scope)
- Model accuracy
- Answer fluency
- Hallucination scoring

These are deferred to Phase 4.
