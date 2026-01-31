from fastapi import FastAPI
from backend.api import ingest, query, version

app = FastAPI(title="Enterprise Knowledge Co-Pilot")

@app.get("/")
def health():
    return {"status": "ok", "service": "Enterprise Knowledge Co-Pilot"}

app.include_router(ingest.router)
app.include_router(query.router)
app.include_router(version.router)
