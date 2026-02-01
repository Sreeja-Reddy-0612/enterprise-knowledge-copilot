from pathlib import Path
from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.versioning.version_manager import get_active_versions
from backend.config import EMBEDDING_MODEL, VECTORSTORE_DIR
from backend.utils.logger import get_logger


def retrieve_context(
    question: str,
    top_k: int = 5,
    override_versions=None,
    trace_id: str | None = None
):
    logger = get_logger("retrieval", trace_id)

    logger.info("Retrieval started")
    logger.info(f"Question = {question}")

    versions = override_versions or get_active_versions()
    logger.info(f"Versions in scope = {versions}")

    results = []

    for version in versions:
        store_path = Path(VECTORSTORE_DIR) / f"{version}.index"

        if not store_path.exists():
            logger.warning(f"Vectorstore missing for version={version}")
            continue

        logger.info(f"Loading vectorstore {store_path}")
        store = FAISSVectorStore(EMBEDDING_MODEL, str(store_path))

        retrieved = store.search_with_scores(question, top_k)
        logger.info(
            f"Retrieved {len(retrieved)} chunks from version={version}"
        )

        for chunk, score in retrieved:
            results.append({
                "text": chunk,
                "score": score,
                "version": version
            })

    results.sort(key=lambda x: x["score"])
    logger.info(f"Total chunks retrieved = {len(results)}")

    return results
