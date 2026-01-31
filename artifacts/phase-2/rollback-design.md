# Rollback Design – Phase 2

## Problem Statement
In production systems, newly ingested knowledge may:
- Contain incorrect data
- Produce degraded retrieval quality
- Break downstream answers

A rollback mechanism is required.

---

## Rollback Strategy

Rollback is achieved by **switching the active version**, not deleting data.

### Steps
1. Identify faulty version
2. Mark version as DEPRECATED
3. Reactivate last known stable version
4. Queries immediately route to stable knowledge

---

## Example

```json
{
  "active_version": "v1.0.0",
  "versions": {
    "v1.0.0": { "status": "ACTIVE" },
    "v1.1.0": { "status": "DEPRECATED" }
  }
}
