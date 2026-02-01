from pathlib import Path
import json

VERSION_REGISTRY_PATH = Path("backend/versioning/versions.json")


class VersionManager:
    def __init__(self):
        VERSION_REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
        if not VERSION_REGISTRY_PATH.exists():
            self._save({
                "active_version": None,
                "versions": {}
            })

    def _load(self):
        return json.loads(VERSION_REGISTRY_PATH.read_text())

    def _save(self, data):
        VERSION_REGISTRY_PATH.write_text(json.dumps(data, indent=2))

    # ---------------------------
    # Registration & lifecycle
    # ---------------------------
    def register_version(self, version: str):
        data = self._load()
        if version not in data["versions"]:
            data["versions"][version] = {"status": "DRAFT"}
        self._save(data)

    def activate_version(self, version: str, exclusive: bool = True):
        data = self._load()
        if version not in data["versions"]:
            raise ValueError("Version does not exist")

        if exclusive:
            for v in data["versions"]:
                data["versions"][v]["status"] = "DEPRECATED"

        data["versions"][version]["status"] = "ACTIVE"
        data["active_version"] = version
        self._save(data)

    def rollback_to(self, version: str):
        self.activate_version(version)

    # ---------------------------
    # Retrieval helpers
    # ---------------------------
    def get_active_version(self):
        return self._load()["active_version"]

    def get_active_versions(self):
        data = self._load()
        return [
            v for v, meta in data["versions"].items()
            if meta["status"] == "ACTIVE"
        ]

    def get_all_versions(self):
        return list(self._load()["versions"].keys())

    def get_version_status(self, version: str):
        return self._load()["versions"].get(version, {}).get("status")


# 🔹 GLOBAL INSTANCE (IMPORTANT)
version_manager = VersionManager()


# 🔹 FUNCTION-LEVEL EXPORTS (for clean imports)
def get_active_versions():
    return version_manager.get_active_versions()

def get_active_version():
    return version_manager.get_active_version()

def rollback_version(version: str):
    version_manager.rollback_to(version)
