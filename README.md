---
title: AI Business Report Analyser
emoji: 📄
colorFrom: blue
colorTo: green
sdk: streamlit
app_file: app.py
tags:
- streamlit
- langchain
- gemini
- rag
pinned: false
short_description: Upload any PDF and ask questions about it
---

# AI Business Report Analyser 📄

An AI-powered document intelligence tool that lets you upload any business PDF and ask questions about it in plain English — built using LangChain, Google Gemini, FAISS, and Streamlit.

---

## What it does

1. Upload any business PDF (annual report, earnings document, research paper)
2. The app chunks the document and builds a searchable vector database
3. Ask any question in plain English
4. The AI retrieves the most relevant sections and generates an accurate answer

---

## How it works

```
PDF Upload
    ↓
Text extraction and chunking (LangChain)
    ↓
Embeddings generated (HuggingFace all-MiniLM-L6-v2)
    ↓
Stored in FAISS vector database
    ↓
User asks a question
    ↓
Relevant chunks retrieved
    ↓
Gemini generates answer from context
```

---

## Tech stack

- **LangChain** — document loading, chunking, and retrieval pipeline
- **Google Gemini API** — LLM for answer generation
- **FAISS** — vector database for semantic search
- **HuggingFace Embeddings** — local embedding model (all-MiniLM-L6-v2)
- **Streamlit** — web interface
- **Python** — core language

---

## Project structure

```
ai-report-analyser/
├── app.py                 # Main Streamlit app
├── utils/
│   ├── chain.py           # LLM chain and retrieval logic
│   └── pdf_loader.py      # PDF loading and chunking
├── requirements.txt       # Dependencies
└── README.md
```

---

## Run locally

```bash
git clone https://github.com/krishiawasthi/AI-report-analyser
cd AI-report-analyser
pip install -r requirements.txt
```

Create a `.env` file:

```
GOOGLE_API_KEY=your_gemini_key
```

Run:

```bash
python3 -m streamlit run app.py
```

---

## Skills demonstrated

- RAG (Retrieval Augmented Generation) pipeline design
- Vector database implementation with FAISS
- Document intelligence and semantic search
- LLM integration with context-aware answer generation
- Python application development and deployment
