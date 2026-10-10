
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
# Find the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent

# Find the data folder
DATA_DIR = BASE_DIR / "data"
# Split long documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# Store all document chunks here
all_chunks = []

# Read each Markdown file
for file_path in sorted(DATA_DIR.glob("*.md")):
    text = file_path.read_text(encoding="utf-8")

    # Convert the text into a Document
    document = Document(
        page_content=text,
        metadata={"source": file_path.name}
    )

    # Split the document into smaller chunks
    chunks = text_splitter.split_documents([document])

    # Add the chunks to our collection
    all_chunks.extend(chunks)

print("Number of documents:", len(list(DATA_DIR.glob("*.md"))))
print("Number of chunks:", len(all_chunks))

# Create a lightweight embedding model for testing
embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")

# Create the Chroma database and save the chunks
vectorstore = Chroma.from_documents(
    documents=all_chunks,
    embedding=embeddings,
    persist_directory=str(BASE_DIR / "chroma_db")
)

print("Documents successfully stored in Chroma!")

