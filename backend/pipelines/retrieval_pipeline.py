from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL
from backend.versioning.version_manager import VersionManager

def retrieve_context(question, knowledge_version, top_k=5):
    store_path = VECTORSTORE_DIR / f"{knowledge_version}.index"

    print("📂 STORE PATH:", store_path)
    print("📦 EXISTS:", store_path.exists())

    store = FAISSVectorStore(EMBEDDING_MODEL, str(store_path))

    results = store.search(question, top_k)

    print("🧠 TOTAL RETRIEVED:", len(results))
    for i, r in enumerate(results):
        print(f"---- CHUNK {i} ----")
        print(r[:300])
        print("------------------")

    return results
