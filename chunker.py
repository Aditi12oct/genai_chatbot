def split_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks
if __name__ == "__main__":
    text = "This is a simple text to demonstrate chunking. " * 50
    chunks = split_text(text)
    for i, c in enumerate(chunks):
        print(f"Chunk {i+1}: {c[:50]}...")

