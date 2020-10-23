from flask import Flask, jsonify, render_template, request
import json
import numpy as np
import pandas as pd
import requests

app = Flask(__name__)



####################### new ########################
@app.route('/')
def index():
  return "Helloooooo"

