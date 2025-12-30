from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


def ask_question(question: str) -> str:
    # Embeddings
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Load vector DB
    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    retriever = db.as_retriever(search_kwargs={"k": 5})

    llm = Ollama(model="llama3")

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a precise academic assistant.

Use ONLY the given context to answer.
If the answer is not found, say "Not found in documents."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    result = qa_chain({"query": question})

    answer = result["result"]

    sources = []
    for doc in result["source_documents"]:
        source = doc.metadata.get("source", "Unknown file")
        page = doc.metadata.get("page", "Unknown page")
        sources.append(f"- {source}, page {page}")

    if sources:
        answer += "\n\nSources:\n" + "\n".join(set(sources))

    return answer