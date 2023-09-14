from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        response = "hola :))"
    return jsonify({"response": response })

if __name__ == "__main__":
    app.run(port=5000, debug=True)