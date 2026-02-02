from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Enterprise Knowledge Co-Pilot"
    environment: str = "local"

    vectorstore_dir: str = "backend/vectorstore"
    versions_file: str = "backend/versioning/versions.json"

    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    max_chunks: int = 5
    similarity_threshold: float = 0.75

    ALLOWED_ORIGINS: list[str] = ["http://localhost:5173"]


settings = Settings()
