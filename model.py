from sentence_transformers import SentenceTransformer
import numpy as np

# Optimized for Render's free tier (400MB RAM usage)
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1: str, text2: str) -> float:
    """Calculate semantic similarity score (0-1) with input truncation"""
    # Truncate to first 512 tokens (~400 words) to handle long paragraphs
    truncated1 = " ".join(text1.split()[:400])
    truncated2 = " ".join(text2.split()[:400])
    
    embeddings = model.encode([truncated1, truncated2])
    cosine_sim = np.dot(embeddings[0], embeddings[1])
    return float(np.clip((cosine_sim + 1) / 2, 0, 1))  # Ensure 0-1 range