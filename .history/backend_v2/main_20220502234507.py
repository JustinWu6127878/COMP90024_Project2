from flask_cors import *
from flask import Flask,render_template,request,Response,redirect,url_for
import json
import couchdb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("../Template/public/index.html")

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=2889,debug=True)