# Hogwart-Project

# 🧠 SLM Multilingual Chatbot (Offline)

This is a multilingual, offline-capable AI chatbot built using:
- 🗂️ LangChain + ChromaDB for RAG (Retrieval-Augmented Generation)
- 🧠 Ollama LLM (Mistral)
- 🌐 Flask for frontend (lightweight)
- 🌍 NLLB-200 for translation (Hindi, Marathi, English)
- 🇮🇳 Optional integration with Bhashini & Indic ecosystem (future scope)

## 🚀 Features
- Document-based answers (PDFs uploaded beforehand by the developer)
- Works fully offline
- Multilingual support (hi, en, mr)
- Gives citations from source files and page numbers

## 📁 File Structure

## 📁 File Structure
├── app.py
├── translator.py
├── rag_chain.py
├── doc_loader.py
├── documents/
├── chroma_db/
├── templates/
│ └── index.html
├── requirements.txt

bash
Copy
Edit

## 🛠️ How to Run
```bash
# Activate virtual environment
source nllb_env/bin/activate

# Run the app
python app.py
Then open http://127.0.0.1:5000 in your browser.

📌 Notes
This chatbot is preloaded with documents — users cannot upload files themselves.

Best used for local governance/PRI projects with offline access needs.

yaml
Copy
Edit

---

### 🟦 3. Save the File

Save the file inside your `Ron` or `SLM_Project` folder.

---

Would you like me to add:
- Your name as author?
- Any links to demo?
- Version info?

Just let me know and I’ll update the README accordingly.
