from pathlib import Path
from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.versioning.version_manager import get_active_version
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL
from backend.utils.logger import get_logger


def retrieve_context(
    question: str,
    top_k: int = 5,
    override_versions=None,
    trace_id: str | None = None,
):
    logger = get_logger("retrieval", trace_id)
    logger.info("Retrieval started")
    logger.info(f"Question = {question}")

    if override_versions:
        versions = override_versions
    else:
        active = get_active_version()
        if not active:
            raise RuntimeError("No active knowledge version")
        versions = [active]

    results = []

    for version in versions:
        store_path = Path(VECTORSTORE_DIR) / f"{version}.index"
        if not store_path.exists():
            continue

        store = FAISSVectorStore(
            embedding_model=EMBEDDING_MODEL,
            index_path=str(store_path),
        )

        retrieved = store.search_with_scores(question, top_k)

        for chunk, score in retrieved:
            results.append({
                "text": chunk,
                "score": score,
                "version": version,
                "trace_id": trace_id,
            })

    results.sort(key=lambda x: x["score"])
    return results
