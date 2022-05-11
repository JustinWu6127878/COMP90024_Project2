from flask_cors import *
from flask import Flask,render_template,request,Response,redirect,url_for
import json
import couchdb

app = Flask(__name__,
            template_folder="dist",
            static_folder="dist/static")

# app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template("index.html")

#for line chart example
@app.route('/chart_data')
def chart_data():
    data_list = {}
    data_line = 100
    data_list['name'] = data_line
    return Response(json.dumps(data_list), mimetype='application/json')

if __name__ == "__main__":
    """run http://127.0.0.1:2889"""
    app.run(host='0.0.0.0', port=2889,debug=True)