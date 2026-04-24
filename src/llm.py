from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )