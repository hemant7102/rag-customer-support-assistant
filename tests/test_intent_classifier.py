from src.intent_classifier import classify_intent


def test_billing_intent():
    intent, esc = classify_intent("refund my money")

    assert intent == "billing"
    assert esc is False


def test_complaint_intent():
    intent, esc = classify_intent("I am very angry")

    assert intent == "complaint"
    assert esc is True