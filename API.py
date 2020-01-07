## importing necessary packages
import flask
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json

# initialize our Flask application and detection model
from sklearn.ensemble import RandomForestClassifier

app = flask.Flask(__name__)
# model = None

"""
function to load our pre-trained detection model and prepare it for inference
"""
# def load_model():
#     global model
#     model = RandomForestClassifier

@app.route('/', methods=['POST'])

def makecalc():
    data = request.get_json()
    print(data)
    ab = model.predict(data)
    # print(ab)
    prediction = np.array2string(ab)

    return jsonify(prediction)


if __name__ == '__main__':
    modelfile = 'finalized_model.sav'
    model = p.load(open(modelfile, 'rb'))
    app.run(host='0.0.0.0')
