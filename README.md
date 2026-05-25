# AI Report Analyser

AI Report Analyser is a Streamlit-based web application that allows users to upload a PDF report and generate AI-powered summaries or answers to questions based on the document content. The project uses LangChain, Gemini API, FAISS vector search, and PDF text extraction to build a simple Retrieval-Augmented Generation (RAG) workflow.

## Project Overview

The goal of this project is to make report analysis faster and easier by allowing users to interact with PDF documents using natural language.

Instead of manually reading long reports, users can upload a PDF and ask questions such as:

- Summarise this document in 5 bullet points
- What are the key findings?
- What are the risks mentioned in the report?
- What recommendations are given?
- Explain this report in simple terms

The application extracts text from the uploaded PDF, splits it into smaller chunks, creates vector embeddings, retrieves the most relevant sections, and sends them to Gemini to generate an answer.

## Features

- Upload PDF reports through a Streamlit interface
- Extract and split PDF text into manageable chunks
- Create vector embeddings using Gemini embeddings
- Store document vectors using FAISS
- Retrieve relevant document sections based on user questions
- Generate AI-based summaries and answers using Gemini
- Keeps API keys secure using a `.env` file
- Simple project structure suitable for learning and portfolio use

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- FAISS
- PyPDF
- python-dotenv
- RAG architecture

## Project Structure

```text
AI-report-analyser/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
└── utils/
    ├── pdf_loader.py
    └── chain.py
