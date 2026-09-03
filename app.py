import os
import tempfile
import streamlit as st

from utils.pdf_loader import load_and_split_pdf
from utils.chain import build_qa_chain

st.set_page_config(page_title="AI Report Analyser", page_icon="📄", layout="centered")
st.title("AI Report Analyser")
st.write("Upload a PDF report and ask questions about it.")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    if "uploaded_file_name" not in st.session_state or st.session_state.uploaded_file_name != uploaded_file.name:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        with st.spinner("Processing PDF — this only happens once..."):
            chunks = load_and_split_pdf(tmp_path)
            st.session_state.chain = build_qa_chain(chunks)
            st.session_state.uploaded_file_name = uploaded_file.name
        st.success("PDF processed and ready.")
    else:
        st.success("PDF already loaded — ask away.")

    chain = st.session_state.chain

    if st.button("Summarise Document"):
        with st.spinner("Summarising..."):
            result = chain("Summarise this document in exactly 5 bullet points.")
            st.subheader("Summary")
            st.write(result.get("result", result) if isinstance(result, dict) else result)

    question = st.text_input("Ask a question about the document")
    if question:
        with st.spinner("Finding answer..."):
            result = chain(question)
            st.subheader("Answer")
            st.write(result.get("result", result) if isinstance(result, dict) else result)
else:
    st.info("Please upload a PDF to begin.")
    for key in ["chain", "uploaded_file_name"]:
        if key in st.session_state:
            del st.session_state[key]