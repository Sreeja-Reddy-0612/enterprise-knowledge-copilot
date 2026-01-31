# Knowledge Versioning Model – Phase 1

## Definition
A knowledge version represents a stable snapshot of enterprise knowledge at a point in time.

## Current Implementation
- Version ID passed explicitly during ingestion
- Each version maps to a separate FAISS index
- Queries must specify the knowledge version
- No cross-version contamination allowed

## Example
- v1.0.0 → policy documents
- v1.1.0 → updated policy documents
- v2.0.0 → restructured or replaced knowledge

## Why Version as Metadata?
- Enables rollback without re-ingestion
- Supports regression comparison across versions
- Decouples system logic from knowledge lifecycle

## Future Extensions
- Version activation states (ACTIVE, DEPRECATED)
- Version comparison and drift detection
- Safe rollback to last stable version
