from flask_cors import *
from flask import Flask,render_template,request,Response,redirect,url_for
import json
import couchdb

app = Flask(__name__,
            template_folder="../Template/dist",
            static_folder="../Template/dist/static")

# app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/wordCloud_data')
def wordCloud_data():
    data_list = {}
    data10 = ['syd','melb', 'perth', 'bris', 'adle', 'other']
    data_list['data_legend'] = data10
        return Response(json.dumps(data_list), mimetype='application/json')



if __name__ == "__main__":
    """run http://127.0.0.1:2889"""
    app.run(host='0.0.0.0', port=2889,debug=True)