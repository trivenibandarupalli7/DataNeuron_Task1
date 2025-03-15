from flask import Flask, request, jsonify
from model import compute_similarity

app = Flask(__name__)

# Health check endpoint (GET)
@app.route('/')
def home():
    return "Semantic Similarity API is running! Use POST /predict with JSON payload"

# Main prediction endpoint (POST)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    score = compute_similarity(text1, text2)
    return jsonify({'similarity_score': round(score, 2)})