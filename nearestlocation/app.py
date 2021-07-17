
from flask import Flask, request
from linebot.models import *
from linebot import *
import json
import requests

app = Flask(__name__)

line_bot_api = LineBotApi('t8TS42nUWRlHempLf4OLMEf1xoNm96YHojEt71MgX96NGuA9qucXNT/4nJtBscYdXZt/ADJLVbqfcwIbdSrlqsW0s0z6i8GPPWtipaaGnOoj0UhNrGI7eeOXAzRf4A6s1hdq+CraBNPxexpYI3TwowdB04t89/1O/w1cDnyilFU=') #Channel Access Token line
handler = WebhookHandler('7f819199fc35d2461ceb0191d0fb304d') #Channel Secret of line

@app.route("/callback", methods=['POST'])

def index():
  return "My first python on Git Heroku"
  #return "Helloooooo"
  
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req['queryResult']['intent']['displayName'] 
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text'] 
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)
    
    reply(intent,text,reply_token,id,disname)

    return 'OK'
    
    
def reply(intent,text,reply_token,id,disname):
    if intent == 'covid':
        data = requests.get('https://covid19.th-stat.com/api/open/today')
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
    app.run()

