from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_vector(text):
    embeddings = model.encode(text)
    return embeddings

if __name__ == '__main__':
    # Example usage
    text = "This is an example sentence."
    vector = generate_vector(text)
    print("Vector:\n", vector)
