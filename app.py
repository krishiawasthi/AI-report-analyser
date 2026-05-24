import os
import tempfile
import streamlit as st

from utils.pdf_loader import load_and_split_pdf
from utils.chain import build_qa_chain


st.set_page_config(
    page_title="AI Report Analyser",
    page_icon="📄",
    layout="centered"
)

st.title("AI Report Analyser")
st.write("Upload a PDF report and ask questions about it.")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.success("PDF uploaded successfully.")

    if st.button("Summarise Document"):
        with st.spinner("Reading and analysing the document..."):
            chunks = load_and_split_pdf(tmp_path)
            chain = build_qa_chain(chunks)

            result = chain("Summarise this document in exactly 5 bullet points.")

            st.subheader("Summary")

            if isinstance(result, dict):
                st.write(result.get("result", result))
            else:
                st.write(result)

    question = st.text_input("Ask a question about the document")

    if question:
        with st.spinner("Finding answer..."):
            chunks = load_and_split_pdf(tmp_path)
            chain = build_qa_chain(chunks)

            result = chain(question)

            st.subheader("Answer")

            if isinstance(result, dict):
                st.write(result.get("result", result))
            else:
                st.write(result)
else:
    st.info("Please upload a PDF to begin.")