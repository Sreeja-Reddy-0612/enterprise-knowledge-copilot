from fastapi import APIRouter
from backend.versioning.version_manager import VersionManager

router = APIRouter(prefix="/version")

@router.get("/active")
def get_active_version():
    vm = VersionManager()
    return {"active_version": vm.get_active_version()}
