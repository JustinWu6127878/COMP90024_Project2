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
@app.route('/wordCloud_data')
def wordCloud_data():
    db_address = 'http://admin:123456@172.26.134.164:5984/'

    try:
        couchServer = couchdb.Server(db_address)
    except Exception as e:
        print(e)

    db = couchServer['Infaltion_result']

    city_count = dict()
    
    for id in db:


    data_list = {}
    data_list['name'] = 100
    return Response(json.dumps(data_list), mimetype='application/json')

if __name__ == "__main__":
    """run http://127.0.0.1:2889"""
    app.run(host='0.0.0.0', port=2889,debug=True)