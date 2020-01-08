import pandas as pd
import numpy as np
from flask import Flask, request ,jsonify
import pickle
import requests

#load model
model = pickle.load(open('finalized_model.sav', 'rb'))

#app
app = Flask(__name__)

#routes
@app.route('/', methods=['POST'])

def predict():
    '''
    For rendering results on HTML GUI
    '''
    #get data
    data = request.get_json(force=True)
    
    #predictions
    result = np.array2string(model.predict(data))
    
    #send back to browser
    output = {'results': int(result[0])}
    
    #return data
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
