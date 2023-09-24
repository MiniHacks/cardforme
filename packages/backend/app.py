from fastapi import FastAPI, Request, Body
import transactions
from pydantic import BaseModel
from card_backtesting import *

app = FastAPI()

class Item(BaseModel):
    flights: float
    groceries: float
    gas: float
    dining: float
    entertainment: float
    car_rental: float
    hotel: float
    retail: float
    digital_wallet: bool
    total: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/get_items")
async def get_items(item: Item):
    return transactions.get_items()

@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()

@app.get("/api/get_transactions")
async def get_transactions(transactions: transactions.Transactions):
    return {transactions: transactions}

