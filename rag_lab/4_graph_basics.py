
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# Define the information passed between graph nodes
class GraphState(TypedDict):
    question: str
    answer: str


# First node: receive the question
def receive_question(state: GraphState):
    print("Step 1: Received the question")
    return {}


# Second node: prepare a simple answer
def answer_question(state: GraphState):
    print("Step 2: Preparing the answer")
    return {"answer": "This is a demonstration answer."}

# Decide whether the question is empty
def check_question(state: GraphState):
    if state["question"].strip():
        return "has_question"
    return "empty_question"


# Create the graph
graph_builder = StateGraph(GraphState)

# Add nodes
graph_builder.add_node("receive", receive_question)
graph_builder.add_node("answer", answer_question)

# Connect the nodes
graph_builder.add_edge(START, "receive")
graph_builder.add_conditional_edges(
    "receive",
    check_question,
    {
        "has_question": "answer",
        "empty_question": END
    }
)

graph_builder.add_edge("answer", END)
# Compile the graph
graph = graph_builder.compile()

# Run the graph
result = graph.invoke({
    "question": "What is RAG?",
    "answer": ""
})

print("\nFinal result:")
print(result)
print("\nGraph diagram:")
print(graph.get_graph().draw_mermaid())