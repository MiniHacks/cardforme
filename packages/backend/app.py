from fastapi import FastAPI
import transactions

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
