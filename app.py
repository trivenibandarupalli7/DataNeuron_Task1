from flask import Flask, request, jsonify
from model import compute_similarity

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    score = compute_similarity(data['text1'], data['text2'])
    return jsonify({'similarity_score': round(score, 2)})

@app.route('/batch', methods=['POST'])
def batch_predict():
    file = request.files['file']
    df = pd.read_csv(file)
    df['score'] = df.apply(lambda row: compute_similarity(row['text1'], row['text2']), axis=1)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)