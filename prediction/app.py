from flask import Flask, request, abort, jsonify, render_template, url_for, redirect
from linebot.models import *
from linebot import *
import json
import requests
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

#get other .py files
from getIP import * #from file getIP.py


app = Flask(__name__)

#model = load_model('deployment_df24072021')
#cols = ['PlaceDeath', 'Sex', 'I10', 'E119', 'E78', 'I21-25', 'N18', 'I61-9', 'UD-CVS-Risk', 'Alcohol-relatedunderlying', 'Numberofunderlyingdisease', 'Age', 'CODAsPDxLast-6-Mo']

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

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('index.html',pred='Expected cause of death would be {}'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)



line_bot_api = LineBotApi('t8TS42nUWRlHempLf4OLMEf1xoNm96YHojEt71MgX96NGuA9qucXNT/4nJtBscYdXZt/ADJLVbqfcwIbdSrlqsW0s0z6i8GPPWtipaaGnOoj0UhNrGI7eeOXAzRf4A6s1hdq+CraBNPxexpYI3TwowdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7f819199fc35d2461ceb0191d0fb304d')


@app.route("/callback", methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
       payload = request.json
       Reply_token = payload['events'][0]['replyToken']
       print(Reply_token)
       message = payload['events'][0]['message']['text']
       print(message)
       if 'ดี' in message :
           Reply_messasge = 'ดีมาก'
           ReplyMessage(Reply_token,Reply_messasge,'t8TS42nUWRlHempLf4OLMEf1xoNm96YHojEt71MgX96NGuA9qucXNT/4nJtBscYdXZt/ADJLVbqfcwIbdSrlqsW0s0z6i8GPPWtipaaGnOoj0UhNrGI7eeOXAzRf4A6s1hdq+CraBNPxexpYI3TwowdB04t89/1O/w1cDnyilFU=') #ใส่ Channel access token
       return request.json, 200
    else:
       abort(400)
def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
     }
     data = {
     "replyToken":Reply_token,
     "messages":[{
      "type":"text",
      "text":TextMessage
      }]
      }
      data = json.dumps(data)
      r = requests.post(LINE_API, headers=headers, data=data)
      return 200


if __name__ == "__main__":
    app.run(debug = True)
