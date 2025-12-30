from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

def get_llm():
    return Ollama(
        model="llama3",
        temperature=0
    )

PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a strict assistant.
Answer the question using ONLY the context below.
If the answer is not present, say: "Not found in documents."

Context:
{context}

Question:
{question}

Answer:
"""
)