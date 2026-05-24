import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


load_dotenv()


def build_qa_chain(chunks):
    """
    Builds a simple Gemini + FAISS retrieval function.
    """

    if not chunks:
        raise ValueError("No document chunks found. Please upload a valid PDF.")

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY is missing. Please add it to your .env file.")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0
    )

    def ask_question(query):
        docs = retriever.invoke(query)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are an AI report analyser. Use only the context below to answer the question.

Context:
{context}

Question:
{query}

Answer clearly and concisely.
"""

        response = llm.invoke(prompt)

        return {
            "result": response.content,
            "source_documents": docs
        }

    return ask_question