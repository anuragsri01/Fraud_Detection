import pickle as p
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/input/', methods=['GET'])
def respond():
    req = request.args.get("input", None)
    print(f"got input{req}")

    response = {}
    return jsonify(req)


@app.route('/predict/', methods=['POST'])
def predict():
    data = request.get_json('req')
    print(data)
    return jsonify(data)


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    model_file = 'finalized_model.sav'
    model = p.load(open(model_file, 'rb'))
    app.run(threaded=True, port=5000)
