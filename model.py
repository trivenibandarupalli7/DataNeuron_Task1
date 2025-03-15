from sentence_transformers import SentenceTransformer

# Cache the lightweight model
model = SentenceTransformer(
    'all-MiniLM-L6-v2',
    device='cpu',  # Force CPU usage to avoid GPU memory issues
    use_auth_token=False
)

def compute_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    return float(np.dot(embeddings[0], embeddings[1]))  # Direct cosine similarity