#!/usr/bin/env python

from fastapi import FastAPI

users = [
    {"id": 0, "role": "absolute", "name": "Vanara"},
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Gerbert"},
    {"id": 3, "role": "trader", "name": "Karlen"},
    {"id": 4, "role": "god", "name": "Jean"}
]

trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 112, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 124, "amount": 2.12},
]

app = FastAPI(title="web_text_out")

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return[user for user in users if user.get("id") == user_id]

@app.get("/trades")
def get_trades(limit: int = 2, offset: int = 0):
    return trades[offset:][:limit]