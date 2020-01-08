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
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #get data
    data = request.get_json(force=True)
    prediction = np.array2string(model.predict(data))
    
    #send back to browser
    output = jsonify(prediction)
    
    #return data
    return render_template('index.html', prediction_text='Transaction is:-'.format(output))

if __name__ == '__main__':
    app.run(debug=True)
