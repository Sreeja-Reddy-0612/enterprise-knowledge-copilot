# backend/versioning/rollback.py

from backend.versioning.version_manager import VersionManager

class RollbackManager:
    def __init__(self):
        self.vm = VersionManager()

    def rollback_to(self, version: str):
        self.vm.activate_version(version)
        self.vm.activate_version(version)
        return {
            "rolled_back_to": version,
            "status": "ACTIVE"
        }
