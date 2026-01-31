from fastapi import APIRouter, UploadFile, Form
import shutil
import os
from backend.pipelines.ingest_pipeline import ingest_document

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile, knowledge_version: str = Form(...)):
    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/{file.filename}"

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    ingest_document(file_path, knowledge_version)
    return {"status": "ingested", "version": knowledge_version}
