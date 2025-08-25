import os
from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Paths
DOCS_DIR = "documents"
CHROMA_DIR = "chroma_db"

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load and chunk documents
def load_documents():
    documents = []
    for file in os.listdir(DOCS_DIR):
        path = os.path.join(DOCS_DIR, file)
        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        else:
            continue
        documents.extend(loader.load())
    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

def create_vector_store():
    docs = load_documents()
    chunks = split_documents(docs)
    vectordb = Chroma.from_documents(documents=chunks, embedding=embedding_model, persist_directory=CHROMA_DIR)
    vectordb.persist()
    print("✅ Vector DB created successfully and saved offline.")

if __name__ == "__main__":
    create_vector_store()
