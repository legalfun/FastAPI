#!/usr/bin/env python
from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

from fastapi import FastAPI

users = [
    {"id": 0, "role": "absolute", "name": "Vanara"},
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Gerbert"},
    {"id": 3, "role": "trader", "name": "Karlen", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
     ]},
    {"id": 4, "role": "god", "name": "Jean"}
]

trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 112, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 124, "amount": 2.12},
]

app = FastAPI(title="web_text_out")

class DegreeType(Enum):
    newbie = "newbe"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in users if user.get("id") == user_id]


currency = ["BTC", "SBER"]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=6)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades_new: List[Trade]):
    trades.extend(trades_new)
    return {"status": 200, "data": trades}
