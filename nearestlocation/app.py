
from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"


#if __name__ == '__main__':
 # app.run(debug=True)

#from flask import Flask #need

#app = Flask(__name__)



####################### new ########################
#@app.route('/')
#def index():
  #return "My first python on Git Heroku"
  #return "Helloooooo"
