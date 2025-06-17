from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import random

quote_api = "https://thequoteshub.com/api/"
app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# get quotes from this api: https://thequoteshub.com/api/
@app.get("/quote")
def get_quote():
    response = requests.get(quote_api)
    print(response)
    if response.status_code == 200:
        data = response.json()
        print(data)
        content = f'{data['text']}\n - {data['author']}'
        return {"quote": content}
    else:
        return {"error": "Failed to fetch quote"}

# quotes = [
#     "Stay hungry, stay foolish.",
#     "Talk is cheap. Show me the code.",
#     "Simplicity is the soul of efficiency."
# ]

# @app.get("/quote")
# def get_quote():
#     return {"quote": random.choice(quotes)}
