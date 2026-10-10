
from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings


# Find the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent


# Load the embedding model
embeddings = FastEmbedEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


# Open the existing Chroma database
vectorstore = Chroma(
    persist_directory=str(BASE_DIR / "chroma_db"),
    embedding_function=embeddings
)


# Tool 1: Search the college knowledge documents
def search_knowledge(question: str):
    results = vectorstore.similarity_search_with_score(
        question,
        k=2
    )

    if not results or results[0][1] > 0.5:
        return "No reliable answer found in the available documents."

    answer = ""

    for document, score in results:
        answer += document.page_content + "\n"
        answer += "Source: " + document.metadata.get("source", "Unknown") + "\n\n"

    return answer


# Tool 2: Store a question in simple conversation memory
conversation_memory = []


def remember_question(question: str):
    conversation_memory.append(question)
    return "Question saved in memory."


# Demonstrate the tools
question = "What is the minimum attendance required for exams?"

print("Question:", question)

print("\nKnowledge search:")
print(search_knowledge(question))

print("Memory:")
print(remember_question(question))
print("Questions remembered:", conversation_memory)