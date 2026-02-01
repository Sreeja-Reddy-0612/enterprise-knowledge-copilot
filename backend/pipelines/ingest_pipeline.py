from backend.utils.pdf_loader import load_pdf_and_chunk
from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL
from backend.versioning.version_manager import VersionManager


def ingest_document(file_path: str, knowledge_version: str):
    chunks = load_pdf_and_chunk(file_path)

    if not chunks:
        raise RuntimeError("PDF contains no extractable text")

    store_path = VECTORSTORE_DIR / f"{knowledge_version}.index"

    store = FAISSVectorStore(
        embedding_model=EMBEDDING_MODEL,
        index_path=str(store_path)
    )

    store.add(chunks)

    # ✅ VERSION REGISTRATION + AUTO ACTIVATE
    vm = VersionManager()
    vm.register_version(knowledge_version)
    vm.activate_version(knowledge_version)

    print(f"Ingested {len(chunks)} chunks")
    print("FIRST CHUNK:", chunks[0][:300])
