# app/schemas/bitcoin.py
from typing import List
from pydantic import BaseModel


class ErrorDetail(BaseModel):
    message: str


class Address(BaseModel):
    addr: str


# BALANCE
class BalanceItem(BaseModel):
    confirmed: int
    addr: str
    unconfirmed: int


class BalanceSchema(BaseModel):
    response: List[BalanceItem]


# HISTORY
class PendingItem(BaseModel):
    status: int
    addr: List[str]
    time: int
    value: int
    txid: str


class HistoryItem(BaseModel):
    time: int
    addr: List[str]
    value: int
    txid: str


class HistorySchema(BaseModel):
    pending: List[PendingItem]
    history: List[HistoryItem]


# TRANSACTION DETAIL
class VoutItem(BaseModel):
    value: int
    address: str


class VinItem(BaseModel):
    value: int
    address: str


class TxnDetailSchema(BaseModel):
    status: str
    fee: int
    vout: List[VoutItem]
    vin: List[VinItem]
    time: int
    size: int


# CURRENCY & PRICE
class CurrencyItem(BaseModel):
    currency_code: str


class CurrencySchema(BaseModel):
    currencies: List[CurrencyItem]


class PriceData(BaseModel):
    price: float
