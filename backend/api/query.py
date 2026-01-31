from fastapi import APIRouter
from backend.models.query import QueryInput
from backend.models.answer import AnswerOutput
from backend.pipelines.retrieval_pipeline import retrieve_context
from backend.pipelines.generation_pipeline import generate_answer

router = APIRouter()

@router.post("/query", response_model=AnswerOutput)
def query(input: QueryInput):
    contexts = retrieve_context(
        input.question,
        input.knowledge_version
    )

    print("RETRIEVED CONTEXTS:")
    for i, c in enumerate(contexts):
        print(f"[{i}]", c[:200])

    result = generate_answer(input.question, contexts)

    return AnswerOutput(
        answer=result["answer"],
        sources=result["sources"],
        knowledge_version=input.knowledge_version
    )
