from fastapi import APIRouter
from backend.models.query import QueryInput
from backend.models.answer import AnswerOutput
from backend.pipelines.retrieval_pipeline import retrieve_context
from backend.pipelines.generation_pipeline import generate_answer

router = APIRouter()

@router.post("/query", response_model=AnswerOutput)
def query(input: QueryInput):
    contexts = retrieve_context(input.question, input.knowledge_version)
    answer = generate_answer(input.question, contexts)

    sources = list(set([c["source"] for c in contexts]))

    return AnswerOutput(
        answer=answer,
        sources=sources,
        knowledge_version=input.knowledge_version
    )
