from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-downloaded model (faster startup)
model = SentenceTransformer(
    'all-MiniLM-L6-v2',
    device="cpu",  # Force CPU usage to save memory
    use_auth_token=False
)

def compute_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return max(0.0, min(1.0, round(similarity, 2)))