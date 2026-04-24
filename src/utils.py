def validate_answer(llm, query, answer, context):
    prompt = f"""
You are a strict evaluator.

Question: {query}

Answer: {answer}

Context: {context}

Reply ONLY:
VALID or INVALID
"""

    result = llm.invoke(prompt).content.strip().upper()
    return "VALID" in result