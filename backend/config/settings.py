from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # App
    app_name: str = "Enterprise Knowledge Co-Pilot"
    environment: str = "local"

    # Paths
    base_dir: Path = Path("backend")
    vectorstore_dir: Path = Path("backend/vectorstore")
    versions_file: Path = Path("backend/versioning/versions.json")

    # Models
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Retrieval
    max_chunks: int = 5
    similarity_threshold: float = 0.75

    # CORS
    allowed_origins: list[str] = ["http://localhost:5173"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
