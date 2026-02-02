CONFIDENCE_THRESHOLD = 1.2   # FAISS L2 distance


def generate_answer(question, retrieved_chunks, trace_id=None):
    """
    Generates grounded answer from retrieved chunks
    """

    answer_text = ""

    if not retrieved_chunks:
        return {
            "answer": "No relevant information found.",
            "sources": [],
            "trace_id": trace_id
        }

    # Simple grounded answer (you can improve later)
    answer_text = "\n".join(
        chunk["text"] for chunk in retrieved_chunks[:5]
    )

    sources = list(set(chunk["version"] for chunk in retrieved_chunks))

    return {
        "answer": answer_text,
        "sources": sources,
        "trace_id": trace_id
    }
