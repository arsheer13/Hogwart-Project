# 🌐 SLM Multilingual Chatbot (Hindi | English | Marathi)

This project is a **document-based, multilingual chatbot** powered by open-source AI models and tools. It supports both **offline and online deployment** and is currently being hosted on **Hugging Face Spaces** using Gradio.

---

## 🧠 Core Technologies

- **LLM Engine:** Ollama (Mistral) for offline response generation
- **RAG:** LangChain + ChromaDB for Retrieval-Augmented Generation
- **Multilingual Translation:** Meta’s [NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M)
- **Deployment (Current):** [Gradio](https://www.gradio.app/) on Hugging Face Spaces
- **Language Support:** Hindi (`hi`), Marathi (`mr`), English (`en`)
- **Optional Integrations (Future):** [Bhashini](https://bhashini.gov.in/), [IndicNLP](https://github.com/AI4Bharat/indicTrans2)

---

## 🚀 Features

- 🔍 **Document-based Q&A:** Uses vector search on preloaded documents (PDF/DOCX)
- 🌐 **Multilingual:** Understands and answers in Hindi, Marathi, or English
- 🧠 **Offline-Capable Architecture:** Can run without internet using Ollama + NLLB
- 📄 **References Provided:** Includes file names and page numbers from sources
- 💬 **Voice & WhatsApp-ready (optional future upgrades)**

---

## 🗂️ Project Structure

├── app.py # Gradio interface logic
├── translator.py # NLLB-200 translation utility
├── rag_chain.py # Retrieval + generation logic using LangChain
├── doc_loader.py # PDF/DOCX parsing and ingestion
├── documents/ # Pre-uploaded document files
├── chroma_db/ # Vector database storage
├── requirements.txt # Python dependencies

yaml
Copy code

---

## 🧪 How to Run Locally

```bash
# 1. Create virtual environment
python3 -m venv nllb_env
source nllb_env/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Gradio app
python app.py
Then open the Gradio link shown in your terminal (typically http://127.0.0.1:7860).

📝 Notes
Users cannot upload their own documents yet; only the developer can preload them.

Designed for low-connectivity governance use-cases (e.g. Gram Panchayats, PRI systems).

Translations are powered by NLLB-200 locally, fetched once and cached.

To save RAM on deployment, make sure model files are pre-cached or compressed.

🧑‍💻 Author
Built with 💡 by Arshee Rizvi
If citing or sharing, please attribute appropriately.
📧 arshee.rizvi@diu.one

