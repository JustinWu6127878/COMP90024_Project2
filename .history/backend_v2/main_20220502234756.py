from flask_cors import *
from flask import Flask,render_template,request,Response,redirect,url_for
import json
import couchdb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("D:\课件\Master\CCC\COMP90024_Project2\Template\public")

if __name__ == "__main__":
    """run http://127.0.0.1:2889"""
    app.run(host='0.0.0.0', port=2889,debug=True)