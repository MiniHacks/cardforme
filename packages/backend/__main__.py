import uvicorn
import backend.app as app
import os
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
async def get_transactions(transactions):
    print(transactions)
    return {transactions: transactions}


if __name__ == "__main__":
    uvicorn.run(app.app, host="0.0.0.0", port=int(os.environ.get("BACKEND_PORT", 8000)))
    res = get_transactions().json()
    current_transactions = Transactions()

    for transaction in res:

        category = transaction['category']
        if len(category) > 1:
            category = category[1]
        else:
            continue

        current_transactions.add_transaction(category, transaction['amount'])


#
#
#
