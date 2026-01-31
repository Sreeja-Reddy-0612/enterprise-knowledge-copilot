# backend/pipelines/generation_pipeline.py

def generate_answer(question, contexts):
    if not contexts:
        return "I don’t have enough approved knowledge to answer this question."

    combined_context = "\n".join([c["text"] for c in contexts])

    # Simple baseline (LLM added later)
    answer = f"Based on the documents:\n{combined_context[:1000]}"

    return answer
