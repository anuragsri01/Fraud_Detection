import pickle as p
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def verify():
    data = request.get_json()
    print(data)
    return jsonify(data)


@app.route('/', methods=['GET'])
def respond():
    data = p.read_csv(
        'https://github.com/anuragsri01/Fraud_Detection/blob/master/check.csv')
    data.head(3)


if __name__ == '__main__':
    model_file = 'finalized_model.sav'
    model = p.load(open(model_file, 'rb'))
    app.run()
