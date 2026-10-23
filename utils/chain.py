import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class GeminiEmbeddings(Embeddings):
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def embed_documents(self, texts):
        return [self._embed(t) for t in texts]

    def embed_query(self, text):
        return self._embed(text)

    def _embed(self, text):
        result = self.client.models.embed_content(
            model="gemini-embedding-exp-03-07",
            contents=text,
        )
        return result.embeddings[0].values

def build_qa_chain(chunks):
    if not chunks:
        raise ValueError("No document chunks found. Please upload a valid PDF.")

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is missing.")

    try:
        embeddings = GeminiEmbeddings(api_key=api_key)
        vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)
    except Exception as e:
        raise ValueError(f"Embedding error: {str(e)}")

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0
    )

    def ask_question(query):
        docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"""You are an AI report analyser. Use only the context below to answer the question.

Context:
{context}

Question:
{query}

Answer clearly and concisely."""
        response = llm.invoke(prompt)
        return {
            "result": response.content,
            "source_documents": docs
        }

    return ask_question