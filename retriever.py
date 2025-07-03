def retrieve_relevant_chunks(vector_store, query, k=3):
    results = vector_store.similarity_search(query, k=k)
    return [r.page_content for r in results]

