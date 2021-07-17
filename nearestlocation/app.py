
from flask import Flask, request, render_template
from linebot.models import *
from linebot import *
import json
import requests

app = Flask(__name__)

line_bot_api = LineBotApi('t8TS42nUWRlHempLf4OLMEf1xoNm96YHojEt71MgX96NGuA9qucXNT/4nJtBscYdXZt/ADJLVbqfcwIbdSrlqsW0s0z6i8GPPWtipaaGnOoj0UhNrGI7eeOXAzRf4A6s1hdq+CraBNPxexpYI3TwowdB04t89/1O/w1cDnyilFU=') #Channel Access Token line
handler = WebhookHandler('7f819199fc35d2461ceb0191d0fb304d') #Channel Secret of line
@app.route("/")
def index():
    return render_template('index.html')
  #return "Helloooooo"


if __name__ == "__main__":
    app.run()

