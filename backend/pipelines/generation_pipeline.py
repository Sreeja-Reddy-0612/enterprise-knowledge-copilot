CONFIDENCE_THRESHOLD = 1.2   # FAISS L2 distance

def generate_answer(question: str, retrieved_chunks: list):
    if not retrieved_chunks:
        return {
            "answer": "I could not find relevant information in the knowledge base.",
            "sources": []
        }

    best = retrieved_chunks[0]

    if best["score"] > CONFIDENCE_THRESHOLD:
        return {
            "answer": "The available information is not confident enough to answer this question.",
            "sources": []
        }

    return {
        "answer": best["text"].strip(),
        "sources": [best["version"]]
    }
