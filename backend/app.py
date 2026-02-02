from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import ingest, query, version
from backend.config.settings import settings

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
    }

app.include_router(ingest.router)
app.include_router(query.router)
app.include_router(version.router)
