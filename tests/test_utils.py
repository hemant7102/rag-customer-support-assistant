from src.utils import validate_answer


def test_validate_answer():
    class MockLLM:
        def invoke(self, prompt):
            return type("Obj", (), {"content": "VALID"})()

    llm = MockLLM()

    result = validate_answer(llm, "q", "a", "c")

    assert result is True