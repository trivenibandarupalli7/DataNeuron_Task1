from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1, text2):
    # Generate embeddings for the input texts
    embeddings = model.encode([text1, text2])
    # Compute cosine similarity between the embeddings
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    # Ensure the score is between 0 and 1
    return max(0.0, min(1.0, round(similarity, 2)))