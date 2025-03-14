from flask import Flask, request, jsonify
from model import compute_similarity
import os

app = Flask(__name__)

@app.route('/similarity', methods=['POST'])
def similarity():
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    score = compute_similarity(text1, text2)
    return jsonify({'similarity score': score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))