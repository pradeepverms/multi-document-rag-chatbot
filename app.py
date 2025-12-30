import streamlit as st
import os

from query import ask_question
from ingest import ingest_documents

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="RAG Chatbot",
    layout="wide"
)

st.title("📄 Multi-Document RAG Chatbot")

# ---------------- Sidebar : PDF Upload ----------------
st.sidebar.header("Upload PDFs")

uploaded_files = st.sidebar.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.sidebar.button("Ingest Documents"):
    if not uploaded_files:
        st.sidebar.warning("Please upload at least one PDF")
    else:
        # create data folder
        os.makedirs("data", exist_ok=True)

        # save uploaded PDFs
        file_paths = []
        for file in uploaded_files:
            file_path = os.path.join("data", file.name)
            with open(file_path, "wb") as f:
                f.write(file.read())
            file_paths.append(file_path)

        # clean old vector db
        if os.path.exists("db"):
            os.system("rm -rf db")

        with st.spinner("Ingesting documents..."):
            ingest_documents(file_paths)

        st.sidebar.success("Documents ingested successfully!")

# ---------------- Question Section ----------------
st.markdown("### Ask a Question")

question = st.text_input("Your question")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            answer = ask_question(question)

        st.markdown("### Answer")
        st.write(answer)