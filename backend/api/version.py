from fastapi import APIRouter
import uuid

from backend.versioning.version_manager import (
    rollback_version,
    get_active_version
)
from backend.utils.logger import get_logger

router = APIRouter(prefix="/version")


@router.get("/active")
def active():
    return {"active_version": get_active_version()}


@router.post("/rollback")
def rollback(payload: dict):
    trace_id = str(uuid.uuid4())
    logger = get_logger("rollback", trace_id)

    target_version = payload["version"]

    logger.info(f"Rollback requested → {target_version}")

    rollback_version(target_version)

    active = get_active_version()
    logger.info(f"Rollback completed. Active version = {active}")

    return {
        "status": "rolled_back",
        "active_version": active,
        "trace_id": trace_id
    }
