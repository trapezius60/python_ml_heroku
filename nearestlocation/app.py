from flask import Flask, request, abort, jsonify, render_template, url_for, redirect
from linebot.models import *
from linebot import *
import json
import requests

#get other .py files
from getIP import * #from file getIP.py


app = Flask(__name__)

#run other .py files on this coding page
app.register_blueprint(getIP) #ให้ file getIP.py เชื่อมกับไฟล์นี้ ในตอนที่ runserver ได้


data = [{
            "update":"21-07-2021"
        },
        {
            "id": 1,
            "activity": "autopsy",
            "case": "3"
        },
        {
            "id": 2,
            "activity": "cfm",
            "case": "5"
        },
        {
            "id": 3,
            "activity": "scene",
            "case": "1"
        }
    ]

#@app.route('/')
#def hello():
 #   return "Hello Flask-Heroku Github Python"
            
@app.route('/')
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

line_bot_api = LineBotApi('t8TS42nUWRlHempLf4OLMEf1xoNm96YHojEt71MgX96NGuA9qucXNT/4nJtBscYdXZt/ADJLVbqfcwIbdSrlqsW0s0z6i8GPPWtipaaGnOoj0UhNrGI7eeOXAzRf4A6s1hdq+CraBNPxexpYI3TwowdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7f819199fc35d2461ceb0191d0fb304d')


@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    return 'OK'


if __name__ == "__main__":
    app.run(debug = True)
