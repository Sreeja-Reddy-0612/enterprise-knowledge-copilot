def generate_answer(question: str, contexts: list[str]):
    if not contexts:
        return {
            "answer": "No relevant information found.",
            "sources": []
        }

    q = question.lower()

    # 🔹 Definition-style questions
    if any(k in q for k in ["what is", "define", "explain"]):
        # Return the most relevant chunk directly
        return {
            "answer": contexts[0].strip(),
            "sources": ["vectorstore"]
        }

    # 🔹 Resume / factual extraction
    if "name" in q:
        return {
            "answer": contexts[0].split("\n")[0],
            "sources": ["vectorstore"]
        }

    if "skill" in q:
        return {
            "answer": contexts[0],
            "sources": ["vectorstore"]
        }

    # 🔹 Default fallback
    return {
        "answer": contexts[0],
        "sources": ["vectorstore"]
    }
