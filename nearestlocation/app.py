import os
import requests
from flask import Flask, jsonify, request

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
    return "Hello Flask-Heroku"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/callback', methods=['POST'])

def callback():

    json_line = request.get_json()

    json_line = json.dumps(json_line)

    decoded = json.loads(json_line)

    user = decoded["events"][0]['replyToken']

    #id=[d['replyToken'] for d in user][0]

    #print(json_line)

    print("ผู้ใช้：",user)

    sendText(user,'งง') # ส่งข้อความ งง

    return '',200

 

def sendText(user, text):

    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer t8TS42nUWRlHempLf4OLMEf1xoNm96YHojEt71MgX96NGuA9qucXNT/4nJtBscYdXZt/ADJLVbqfcwIbdSrlqsW0s0z6i8GPPWtipaaGnOoj0UhNrGI7eeOXAzRf4A6s1hdq+CraBNPxexpYI3TwowdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป

 

    headers = {

        'Content-Type': 'application/json; charset=UTF-8',

        'Authorization':Authorization

    }

 

    data = json.dumps({

        "replyToken":user,

        "messages":[{

            "type":"text",

            "text":text

        }]

    })

 

    #print("ข้อมูล：",data)

    r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

    #print(r.text)

if __name__ == "__main__":
    app.run(debug=False)
