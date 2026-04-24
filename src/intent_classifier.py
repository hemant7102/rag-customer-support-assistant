def classify_intent(query):
    q = query.lower()

    if "refund" in q or "payment" in q:
        return "billing", False

    if "error" in q or "issue" in q:
        return "technical", False

    if "angry" in q or "complaint" in q:
        return "complaint", True

    return "general", False