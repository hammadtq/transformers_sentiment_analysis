from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

nlp = pipeline("sentiment-analysis")

@app.route('/predict', methods=['POST'])
def predict():
    sentence = request.json.get("sentence", "")
    result = nlp(sentence)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

