from backend.utils.pdf_loader import load_pdf_and_chunk
from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL

def ingest_document(file_path: str, knowledge_version: str):
    chunks = load_pdf_and_chunk(file_path)

    if not chunks:
        raise RuntimeError("No text found in PDF")

    VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)
    store_path = VECTORSTORE_DIR / f"{knowledge_version}.index"

    store = FAISSVectorStore(EMBEDDING_MODEL, str(store_path))
    store.add(chunks)

    print(f"Ingested {len(chunks)} chunks")
    print("FIRST CHUNK:", chunks[0][:300])
