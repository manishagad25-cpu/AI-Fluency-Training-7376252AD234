
from pathlib import Path
from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent

# Load the same embedding model used during ingestion
embeddings = FastEmbedEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# Open the Chroma database
vectorstore = Chroma(
    persist_directory=str(BASE_DIR / "chroma_db"),
    embedding_function=embeddings
)

# Ask a question
question = "What is the minimum attendance required for exams?""
# Retrieve the two most relevant chunks
results = vectorstore.similarity_search_with_score(
    question,
    k=2
)
# Check whether the best search result is relevant
if not results or results[0][1] > 0.5:
    print("Answer: I don't know based on the available documents.")
    raise SystemExit

# Build the context from retrieved documents
context = "\n\n".join(
    document.page_content for document, score in results
)

# Display the question and retrieved context
print("Question:", question)
print("\nRetrieved context:")
print(context)

print("\nSources:")
for document, score in results:
    print("-", document.metadata.get("source", "Unknown"))