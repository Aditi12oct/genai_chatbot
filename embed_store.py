from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")


def create_vector_store(chunks):
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    return vector_store
