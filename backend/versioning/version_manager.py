# backend/versioning/version_manager.py

from pathlib import Path
import json

VERSION_REGISTRY_PATH = Path("backend/versioning/versions.json")

class VersionManager:
    def __init__(self):
        VERSION_REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
        if not VERSION_REGISTRY_PATH.exists():
            self._save({"active_version": None, "versions": {}})

    def _load(self):
        return json.loads(VERSION_REGISTRY_PATH.read_text())

    def _save(self, data):
        VERSION_REGISTRY_PATH.write_text(json.dumps(data, indent=2))

    def register_version(self, version: str):
        data = self._load()
        if version not in data["versions"]:
            data["versions"][version] = {
                "status": "DRAFT"
            }
        self._save(data)

    def activate_version(self, version: str):
        data = self._load()
        if version not in data["versions"]:
            raise ValueError("Version does not exist")

        for v in data["versions"]:
            data["versions"][v]["status"] = "DEPRECATED"

        data["versions"][version]["status"] = "ACTIVE"
        data["active_version"] = version
        self._save(data)

    def get_active_version(self):
        data = self._load()
        return data["active_version"]

    def get_version_status(self, version: str):
        data = self._load()
        return data["versions"].get(version, {}).get("status")
