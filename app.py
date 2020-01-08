
from flask import Flask, request ,jsonify
import random
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def verify():
    data = request.get_json()
    print(data)
    return jsonify(data)

@app.route('/detect', methods=['GET'])
def returnAll():
    return jsonify({'detect': app})

if __name__ == '__main__':
    modelfile = 'finalized_model.sav'
    model = p.load(open(modelfile, 'rb'))
    app.run()
