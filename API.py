

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
