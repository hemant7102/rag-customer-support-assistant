from src.graph_workflow import run_graph

history = []

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    result = run_graph(query, history)
    print("Bot:", result["response"])