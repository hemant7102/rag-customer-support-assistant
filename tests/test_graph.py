from src.graph_workflow import run_graph


def test_run_graph_basic():
    result = run_graph("reset password", [])

    assert "response" in result
    assert isinstance(result["response"], str)