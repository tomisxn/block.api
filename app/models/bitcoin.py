# app/models/bitcoin.py
from pydantic import BaseModel


class Balance(BaseModel):
    addr: str
