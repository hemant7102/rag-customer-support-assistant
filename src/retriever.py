def retrieve(db, query, k=6):
    results = db.similarity_search_with_score(query, k=k)

    filtered = []
    for doc, score in results:
        if score < 1.5:
            filtered.append((doc, score))

    return filtered[:5]


def format_context(results):
    return "\n\n".join([doc.page_content for doc, _ in results])


def compute_confidence(results):
    if not results:
        return "LOW"

    scores = [score for _, score in results]
    avg_score = sum(scores) / len(scores)
    best_score = results[0][1]
    num_docs = len(results)

    if best_score < 0.5 and num_docs >= 3:
        return "HIGH"
    elif avg_score < 1.0:
        return "MEDIUM"
    else:
        return "LOW"


# 🔥 NEW: clean sources
def format_sources(results):
    cleaned = []
    for doc, _ in results:
        text = doc.page_content.strip().replace("\n", " ")
        cleaned.append(text[:300] + "...")
    return cleaned