# backend/pipelines/ingest_pipeline.py

import os
from backend.utils.document_loader import load_pdf
from backend.utils.chunking import chunk_text
from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL

def ingest_document(file_path: str, knowledge_version: str):
    text = load_pdf(file_path)
    chunks = chunk_text(text)

    metadatas = [
        {
            "text": chunk,
            "source": os.path.basename(file_path),
            "knowledge_version": knowledge_version
        }
        for chunk in chunks
    ]

    os.makedirs(VECTORSTORE_DIR, exist_ok=True)
    store_path = VECTORSTORE_DIR / f"{knowledge_version}.index"

    store = FAISSVectorStore(EMBEDDING_MODEL, str(store_path))
    store.add(chunks, metadatas)
