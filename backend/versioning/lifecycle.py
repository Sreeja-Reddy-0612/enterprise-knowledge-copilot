# backend/versioning/lifecycle.py

from backend.versioning.version_manager import VersionManager

def promote_version(version: str):
    vm = VersionManager()
    vm.register_version(version)
    vm.activate_version(version)
