from flask import Flask, request, jsonify
from model import compute_similarity
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def similarity():
    # Extract text1 and text2 from the request
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    
    # Compute similarity score
    score = compute_similarity(text1, text2)
    
    # Return the score in the required format
    return jsonify({'similarity score': score})

if __name__ == '__main__':
    # Run the app on Render's assigned port
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))