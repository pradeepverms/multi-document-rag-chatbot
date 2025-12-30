# Multi-Document RAG Chatbot (Local LLM)

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot that allows users to upload multiple PDFs and ask contextual questions using a **local LLM (Ollama + LLaMA 3)**.

This project demonstrates how to build a **fully offline RAG system** without using paid APIs like OpenAI.

---

## 🚀 Features

- Upload and process **multiple PDF documents**
- Ask questions across all uploaded documents
- Semantic search using **ChromaDB**
- Local embeddings using **nomic-embed-text**
- Local LLM inference using **Ollama (LLaMA 3)**
- Interactive **Streamlit Chat UI**
- No internet or paid API required

---

## 🧠 Tech Stack

- Python
- LangChain
- Ollama
- LLaMA 3
- ChromaDB
- Streamlit

---

## 📁 Project Structure

llm-rag-system/ │ ├── app.py       
# Streamlit UI ├── ingest.py      
# PDF ingestion logic ├── query.py       
# Question answering ├── rag_ollama.py   
# LLM + retriever setup ├── data/       
# Uploaded PDFs ├── db/            
# Vector database └── README.md

---

## ⚙️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

 ollama pull llama3
 python ingest.py
 streamlit run app.py
 
 👨‍💻 Author
Pradip Verma
B.Tech AI & Data Science
Interested in LLMs, RAG systems & AI products
