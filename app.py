import pickle as p
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def verify():
    data = request.get_json()
    print(data)
    return jsonify(data)


@app.route('/', methods=['GET'])
def respond():
    req = request.args
    print(req)
    return jsonify(req)


if __name__ == '__main__':
    model_file = 'finalized_model.sav'
    model = p.load(open(model_file, 'rb'))
    app.run()
