
from flask import Flask, request ,jsonify
import random
import requests

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])                                                                                                    
def add():                                                                                                                              
    data = request.get_json()
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    return jsonify(data)



if __name__ == '__main__':
    modelfile = 'finalized_model.sav'
    model = p.load(open(modelfile, 'rb'))
    app.run()
