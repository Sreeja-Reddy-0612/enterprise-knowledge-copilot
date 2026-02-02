from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import ingest, query, version

app = FastAPI(title="Enterprise Knowledge Co-Pilot")

# 🔐 CORS (Frontend → Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok", "service": "Enterprise Knowledge Co-Pilot"}

app.include_router(ingest.router)
app.include_router(query.router)
app.include_router(version.router)
