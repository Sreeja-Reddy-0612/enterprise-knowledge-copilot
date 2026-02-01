from fastapi import APIRouter
import uuid

from backend.pipelines.retrieval_pipeline import retrieve_context
from backend.pipelines.generation_pipeline import generate_answer
from backend.utils.logger import get_logger

router = APIRouter()


@router.post("/query")
def query(payload: dict):
    trace_id = payload.get("trace_id") or str(uuid.uuid4())
    logger = get_logger("query_api", trace_id)

    question = payload["question"]
    override_versions = payload.get("versions")

    logger.info("Query received")
    logger.info(f"Override versions = {override_versions}")

    retrieved = retrieve_context(
        question=question,
        override_versions=override_versions,
        trace_id=trace_id
    )

    response = generate_answer(question, retrieved)

    used_versions = list(set(r["version"] for r in retrieved))
    logger.info(f"Answer sourced from versions = {used_versions}")

    return {
        **response,
        "knowledge_version": used_versions,
        "trace_id": trace_id
    }
