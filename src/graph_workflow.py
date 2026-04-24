from src.llm import get_llm, get_embeddings
from src.vector_store import init_db, get_db
from src.retriever import retrieve, format_context, compute_confidence, format_sources
from src.intent_classifier import classify_intent
from src.utils import validate_answer
from src.document_processor import process_uploaded_file


def initialize_db(file_path):
    embeddings = get_embeddings()
    chunks = process_uploaded_file(file_path)
    init_db(chunks, embeddings)


def run_graph(query, history):
    embeddings = get_embeddings()

    intent, force = classify_intent(query)

    if force:
        return {
            "response": "Escalated due to user intent.",
            "needs_escalation": True,
            "confidence": "LOW",
            "sources": []
        }

    db = get_db(embeddings)
    results = retrieve(db, query)

    if not results:
        return {
            "response": "No relevant context found. Escalating.",
            "needs_escalation": True,
            "confidence": "LOW",
            "sources": []
        }

    context = format_context(results)
    confidence = compute_confidence(results)

    llm = get_llm()

    # 🔥 STRICT PROMPT
    answer = llm.invoke(
        f"""
You are a strict technical assistant.

Use ONLY the context below.

Context:
{context}

Question:
{query}

Rules:
- Answer must be grounded in context
- Use exact terminology
- Do NOT generalize
- If answer not found, say: "Not found in context"

Answer:
"""
    ).content

    if not validate_answer(llm, query, answer, context):
        return {
            "response": "Answer not reliable. Escalating.",
            "needs_escalation": True,
            "confidence": "LOW",
            "sources": []
        }

    return {
        "response": answer,
        "needs_escalation": False,
        "confidence": confidence,
        "sources": format_sources(results)
    }