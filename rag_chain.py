from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embedding_model)
    return vectordb

def retrieve_context(query: str, k: int = 3):
    vectordb = get_vectorstore()
    results = vectordb.similarity_search_with_score(query, k=k)

    context = ""
    references = []

    for doc, score in results:
        context += doc.page_content + "\n\n"
        metadata = doc.metadata
        file_name = metadata.get("source", "Unknown").split("/")[-1]
        page = metadata.get("page", "N/A")
        references.append(f"{file_name}, Page {page}")

    return context, references

def generate_response(question, context, model_name="mistral"):
    llm = Ollama(model=model_name, temperature=0.2)

    template = """
You are an AI assistant that strictly answers questions only from the given document context.

🛑 If the answer is not present in the context, say:
"The information is not present in the uploaded documents, so I am unable to answer."

✅ If the answer is present, follow these:
- Give a well-explained and structured answer
- Use bullet points where helpful
- Use only the document context below (no general knowledge)
- Do NOT add in-line citations; list references at the end only

📄 Document Context:
{context}

❓User's Question:
{question}

Answer:
"""
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    return chain.invoke({"context": context, "question": question})
