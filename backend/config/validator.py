from backend.config.settings import settings
from backend.utils.logger import get_logger


def validate_runtime_config():
    """
    Fail-fast validation for required runtime configuration.
    This runs ONCE during application startup.
    """
    logger = get_logger("config")

    logger.info("Validating runtime configuration")

    required_fields = {
        "embedding_model": settings.embedding_model,
        "vectorstore_dir": settings.vectorstore_dir,
        "versions_file": settings.versions_file,
    }

    missing = [k for k, v in required_fields.items() if not v]

    if missing:
        raise RuntimeError(
            f"Missing required configuration fields: {missing}"
        )

    logger.info("Runtime configuration validated successfully")

    # Safe config snapshot (NO secrets)
    logger.info(
        {
            "environment": settings.environment,
            "embedding_model": settings.embedding_model,
            "vectorstore_dir": settings.vectorstore_dir,
        }
    )
