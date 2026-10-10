
from pathlib import Path
from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent

# Load the same embedding setup used during ingestion
embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")

# Open the existing Chroma database
vectorstore = Chroma(
    persist_directory=str(BASE_DIR / "chroma_db"),
    embedding_function=embeddings
)

# Ask a question
question = "What is the minimum attendance required for exams?"

# Search for the most relevant document chunks
results = vectorstore.similarity_search_with_score(question, k=3)

# Display the results
for document, score in results:
    print("\nSource:", document.metadata.get("source", "Unknown"))
    print("Score:", score)
    print("Content:", document.page_content)