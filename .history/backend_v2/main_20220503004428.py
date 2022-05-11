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
    var JsonList = [
    {name: "龙头镇", value: "111"},
    {name: "大埔镇", value: "222"},
    {name: "太平镇", value: "458"},
    {name: "沙埔镇", value: "445"},
    {name: "东泉镇", value: "456"},
    {name: "凤山镇", value: "647"},
    {name: "六塘镇", value: "189"},
    {name: "冲脉镇", value: "864"},
    {name: "寨隆镇", value: "652"},
];

if __name__ == "__main__":
    """run http://127.0.0.1:2889"""
    app.run(host='0.0.0.0', port=2889,debug=True)