from fastapi import FastAPI
from backend.api import ingest, query

app = FastAPI(title="Enterprise Knowledge Co-Pilot")

app.include_router(ingest.router)
app.include_router(query.router)
