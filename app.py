from flask import Flask, request, jsonify
from model import compute_similarity
import os

app = Flask(__name__)

@app.route('/similarity', methods=['POST'])
def similarity():
    # Get JSON data from the request
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    # Compute similarity score
    score = compute_similarity(text1, text2)
    # Return the score as JSON
    return jsonify({'similarity score': score})

if __name__ == '__main__':
    # Run the app on the specified port
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))