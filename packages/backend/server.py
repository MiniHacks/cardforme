from dotenv import load_dotenv
import base64
import os
import datetime as dt
import json
import time
# from flask_cors import CORS

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import requests

load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello World!'

@app.route('/api/transactions', methods=['GET', 'POST'])
@cross_origin()
def get_transactions():
    req = request.json
    return jsonify(req)

if __name__ == '__main__':
     app.run(debug=True, port=int(os.getenv('PORT', 8000)))

