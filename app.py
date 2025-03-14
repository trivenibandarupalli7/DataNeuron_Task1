from flask import Flask, request, jsonify
from model import compute_similarity

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def similarity():
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    score = compute_similarity(text1, text2)
    return jsonify({'similarity score': score})

# Remove the `if __name__ == '__main__'` block