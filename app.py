import pandas as pd
import numpy as np
from flask import Flask, request ,jsonify
import pickle
import requests

#app
app = Flask(__name__)
#load model
model = pickle.load(open('finalized_model.sav', 'rb'))

#routes
@app.route('/')
def predict():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)


if __name__ == '__main__':
    app.run(debug=True)
