from backend.utils.logger import get_logger


def generate_answer(question: str, retrieved_chunks: list, trace_id: str):
    logger = get_logger("generation", trace_id)

    if not retrieved_chunks:
        return {
            "answer": "No relevant information found.",
            "sources": [],
        }

    context = "\n".join([c["text"] for c in retrieved_chunks])

    answer = f"Based on the documents:\n\n{context[:2000]}"

    return {
        "answer": answer,
        "sources": retrieved_chunks,
    }
