from flask import Flask, request, abort, jsonify
from linebot.models import *
from linebot import *
import json
import requests

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku Github Python"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)


line_bot_api = LineBotApi('t8TS42nUWRlHempLf4OLMEf1xoNm96YHojEt71MgX96NGuA9qucXNT/4nJtBscYdXZt/ADJLVbqfcwIbdSrlqsW0s0z6i8GPPWtipaaGnOoj0UhNrGI7eeOXAzRf4A6s1hdq+CraBNPxexpYI3TwowdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7f819199fc35d2461ceb0191d0fb304d')


@app.route('/callback', methods=['POST', 'GET'])
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req['queryResult']['intent']['displayName'] 
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text'] 
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    userid = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + userid)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)
    
    reply(intent,text,reply_token,userid,disname)

    return 'OK'
    
    
def reply(intent,text,reply_token,userid,disname):
    if intent == 'covid':
        data = requests.get('https://covid19.th-stat.com/json/covid19v2/getTodayCases.json')
        json_data = json.loads(data.text)
        Confirmed = json_data['Confirmed']  # ติดเชื้อสะสม
        Recovered = json_data['Recovered']  # หายแล้ว
        Hospitalized = json_data['Hospitalized']  # รักษาอยู่ใน รพ.
        Deaths = json_data['Deaths']  # เสียชีวิต
        NewConfirmed = json_data['NewConfirmed']  # บวกเพิ่ม
        text_message = TextSendMessage(
            text='ติดเชื้อสะสม = {} คน(+เพิ่ม{})\nหายแล้ว = {} คน\nรักษาอยู่ใน รพ. = {} คน\nเสียชีวิต = {} คน'.format(
                Confirmed, NewConfirmed, Recovered, Hospitalized, Deaths))

        line_bot_api.reply_message(reply_token, text_message)

if __name__ == "__main__":
    app.run(debug = True)
