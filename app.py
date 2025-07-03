import streamlit as st
from Scraper import scrape_page
from chunker import split_text
from embed_store import create_vector_store
from retriever import retrieve_relevant_chunks
from generator import generate_answer

# Load vector store once
@st.cache_resource
def load_vector_store():
    url = "https://en.wikipedia.org/wiki/Generative_AI"
    st.write(f"Scraping URL: {url}")
    raw_text = scrape_page(url)
    chunks = split_text(raw_text)
    vector_store = create_vector_store(chunks)
    return vector_store

st.title("🔮 GenAI RAG Chatbot")

st.markdown(
    """
This chatbot uses:
- A Retriever (FAISS) to fetch relevant text
- gemini to generate answers
"""
)

vector_store = load_vector_store()

query = st.text_input("Ask something about Generative AI:")

if query:
    st.write("🔍 **Searching for context...**")
    retrieved_chunks = retrieve_relevant_chunks(vector_store, query)
    context = "\n\n".join(retrieved_chunks)
    st.write("✅ **Generating answer...**")
    answer = generate_answer(query, context)
    st.write("### ✨ Answer")
    st.write(answer)
