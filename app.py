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
    final_features = np.array2string(data)
    
    #predictions
    result = model.predict(final_features)
    
    #send back to browser
    output = jsonify(prediction)
    
    #return data
    return render_template('index.html', prediction_text='Transaction is:-'.format(output))

if __name__ == '__main__':
    app.run(debug=True)
