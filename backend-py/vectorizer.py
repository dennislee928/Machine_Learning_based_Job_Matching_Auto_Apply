from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def vectorize_text(text):
    embeddings = model.encode(text)
    return embeddings

if __name__ == '__main__':
    # Example usage
    text = "This is an example sentence."
    vector = vectorize_text(text)
    print("Vector:\n", vector)
