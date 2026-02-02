from fastapi import APIRouter
from backend.pipelines.retrieval_pipeline import retrieve_context
from backend.pipelines.generation_pipeline import generate_answer
from backend.utils.logger import get_logger, new_trace_id

router = APIRouter()

@router.post("/query")
def query(payload: dict):
    trace_id = payload.get("trace_id") or new_trace_id()
    logger = get_logger("query_api", trace_id)

    question = payload["question"]
    override_versions = payload.get("versions")

    logger.info("Query received")
    logger.info(f"Override versions = {override_versions}")

    retrieved = retrieve_context(
        question,
        override_versions=override_versions,
        trace_id=trace_id
    )

    response = generate_answer(question, retrieved, trace_id)

    return {
        "answer": response["answer"],
        "sources": response["sources"],
        "knowledge_versions": list(set(r["version"] for r in retrieved)),
        "trace_id": trace_id
    }
