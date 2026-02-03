from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import ingest, query, version
from backend.config.settings import settings
from backend.config.validator import validate_runtime_config


# 🚨 FAIL FAST BEFORE APP STARTS
validate_runtime_config()

app = FastAPI(title=settings.app_name)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
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


# Routers
app.include_router(ingest.router)
app.include_router(query.router)
app.include_router(version.router)
