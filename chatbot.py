from Scraper import scrape_page
from chunker import split_text
from embed_store import create_vector_store
from retriever import retrieve_relevant_chunks
from generator import generate_answer

def main():
    # Scrape content
    url = "https://en.wikipedia.org/wiki/Generative_AI"
    raw_text = scrape_page(url)
    chunks = split_text(raw_text)
    print(f"Loaded {len(chunks)} chunks.")

    # Create vector store
    vector_store = create_vector_store(chunks)

    print("\n✅ Chatbot is ready! Type 'exit' to quit.\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        retrieved_chunks = retrieve_relevant_chunks(vector_store, query)
        context = "\n\n".join(retrieved_chunks)
        answer = generate_answer(query, context)
        print(f"\nBot: {answer}\n")
if __name__ == "__main__":
    main()

