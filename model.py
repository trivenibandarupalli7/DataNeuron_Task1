from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1, text2):
    # Generate embeddings for the two texts
    embeddings = model.encode([text1, text2])
    
    # Compute cosine similarity
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    # Clamp score between 0 and 1, and round to 2 decimals
    return max(0.0, min(1.0, round(similarity, 2)))