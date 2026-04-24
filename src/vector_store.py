from langchain_chroma import Chroma
import os
import shutil

DB_DIR = "chroma_db"


def init_db(chunks, embeddings):
    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)

    return Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_DIR
    )


def get_db(embeddings):
    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )