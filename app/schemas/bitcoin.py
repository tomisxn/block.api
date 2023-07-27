# app/schemas/bitcoin.py
from typing import List
from pydantic import BaseModel


class ErrorDetail(BaseModel):
    message: str


class BalanceBody(BaseModel):
    addr: str


class BalanceResponse(BaseModel):
    confirmed: int
    addr: str
    unconfirmed: int


class BalanceDataResponse(BaseModel):
    response: List[BalanceResponse]
