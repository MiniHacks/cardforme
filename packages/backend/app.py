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



# from fastapi import FastAPI, Request, Body
# import transactions
# from pydantic import BaseModel
# from card_backtesting import *
#
# app = FastAPI()
#
# class Item(BaseModel):
#     flights: float
#     groceries: float
#     gas: float
#     dining: float
#     entertainment: float
#     car_rental: float
#     hotel: float
#     retail: float
#     digital_wallet: bool
#     total: float
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# @app.post("/api/get_items")
# async def get_items(item: Item):
#     return transactions.get_items()
#
# @app.post("/dummypath")
# async def get_body(request: Request):
#     return await request.json()
#
# @app.get("/api/get_transactions")
# async def get_transactions(transactions: transactions.Transactions):
#     return {transactions: transactions}

