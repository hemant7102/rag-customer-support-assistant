from src.retriever import format_context


def test_format_context():
    mock_doc = type("Doc", (), {"page_content": "hello world"})()
    results = [(mock_doc, 0.2)]

    context = format_context(results)

    assert "hello world" in context