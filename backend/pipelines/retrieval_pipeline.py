# backend/pipelines/retrieval_pipeline.py

from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL

def retrieve_context(question, knowledge_version, top_k=5):
    store_path = VECTORSTORE_DIR / f"{knowledge_version}.index"

    if not store_path.exists():
        return []

    store = FAISSVectorStore(EMBEDDING_MODEL, str(store_path))
    results = store.search(question, top_k)

    return results