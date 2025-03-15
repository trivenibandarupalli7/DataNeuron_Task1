from flask import Flask, request, jsonify
from model import compute_similarity
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Semantic Similarity API - Use POST /predict with {'text1':'...','text2':'...'}"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or 'text1' not in data or 'text2' not in data:
            return jsonify({"error": "Invalid request format"}), 400
            
        return jsonify({
            "similarity score": round(compute_similarity(
                data['text1'], 
                data['text2']
            ), 2)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))