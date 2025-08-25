from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model and vector DB
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="backend/chroma_db", embedding_function=embedding_model)

# Print document count
print(f"✅ Total documents loaded in ChromaDB: {vectordb._collection.count()}")
