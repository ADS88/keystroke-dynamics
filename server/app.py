from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

sentences = [
  (0, 'Who washes the windows by Harold the fox'), 
  (1, 'The quick brown fox washes the dishes and stares out Wendy’s window.'), 
  (2, 'Humpdy Dumpty washes windows and jumps over the wall.'), 
  (3, 'Windows by the sea shore require regular washes to see out.')
]

@app.route("/sentence", methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    id, sentence = random.choice(sentences)
    return jsonify(id=id, text=sentence)
  return jsonify(['Andrewe', 'Frankie', 'Arya'])

if __name__ == "__main__":
    app.run(debug=True)
