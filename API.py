## importing necessary packages
import flask
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json

# initialize our Flask application and detection model
from sklearn.ensemble import RandomForestClassifier

from flask import Flask ,request

app = Flask(_name_)

@app.route("/")
def index():
    return "Method used: %s" % request.method

@app.route("/detect", methods=['GET' , 'POST'])
def detect():
    if request.method == 'post':
        return "You are using post"
    else:
        return "Your are using next time post"

if _name_ == "__main__"
    app.run()
