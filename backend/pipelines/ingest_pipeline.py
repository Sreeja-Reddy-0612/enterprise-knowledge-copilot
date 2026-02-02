from backend.utils.pdf_loader import load_pdf_and_chunk
from backend.vectorstore.faiss_store import FAISSVectorStore
from backend.config import VECTORSTORE_DIR, EMBEDDING_MODEL
from backend.versioning.version_manager import VersionManager
from backend.utils.logger import get_logger


def ingest_document(file_path: str, knowledge_version: str):
    logger = get_logger("ingest")

    chunks = load_pdf_and_chunk(file_path)
    if not chunks:
        raise RuntimeError("PDF contains no extractable text")

    store_path = VECTORSTORE_DIR + f"/{knowledge_version}.index"

    store = FAISSVectorStore(
        embedding_model=EMBEDDING_MODEL,
        index_path=store_path,
    )

    store.add(chunks)

    vm = VersionManager()
    vm.register_version(knowledge_version)
    vm.activate_version(knowledge_version)

    logger.info(f"Ingested {len(chunks)} chunks")
    logger.info(f"Active version set to {knowledge_version}")
