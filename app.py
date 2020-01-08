import pandad as pd
from flask import Flask, request ,jsonify
import random
import pickle
import requests

#load model
model = pickle.load(open('finalized_model.sav', 'rb'))

#app
app = Flask(__name__)

#routes
@app.route('/', methods=['POST'])

def predict():
    #get data
    data = request.get_json(force=True)
    
    #convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)
    
    #predictions
    result = model.predict(data_df)
    
    #send back to browser
    output = {'results': int(result[0])}
    
    #return data
    return jsonify(results=output)

if __name__ == '__main__':
#     modelfile = 'finalized_model.sav'
#     model = p.load(open(modelfile, 'rb'))
    app.run()
