# app/routes/bitcoin.py
import json
import requests
from fastapi import APIRouter, HTTPException

from app.config import *
from app.schemas.bitcoin import Address, BalanceSchema, HistorySchema, TxnDetailSchema, CurrencySchema, PriceData

router = APIRouter()


@router.post("/balance", summary="Returns balance and unconfirmed amount(Amount waiting 2 confirmations) of multiple "
                                 "addresses/xpubs", response_model=BalanceSchema)
def get_balance(payload: Address):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + B_API_KEY
    }
    data = json.dumps({
        "addr": payload.addr,
    })

    try:
        response = requests.post(B_BALANCE, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception if the request was not successful

        data = response.json()  # Extract the JSON data from the response
        return data
    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Request Error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected Error")


@router.post("/history", summary="Returns transaction history of multiple bitcoin addresses/xpubs",
             response_model=HistorySchema)
def get_history(payload: Address):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + B_API_KEY
    }
    data = json.dumps({
        "addr": payload.addr,
    })

    try:
        response = requests.post(B_HISTORY, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception if the request was not successful

        data = response.json()  # Extract the JSON data from the response
        return data
    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Request Error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected Error")


@router.get("/tx_detail", summary="Returns detail of input transaction id", response_model=TxnDetailSchema)
def get_balance(txid: str):

    try:
        response = requests.get(B_TXN_DETAIL+"?txid="+txid)
        response.raise_for_status()  # Raise an exception if the request was not successful

        data = response.json()  # Extract the JSON data from the response
        return data
    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected Error")


@router.get("/currencies", summary="Returns all currencies")
def get_currencies():

    try:
        response = requests.get(B_CURRENCIES)
        response.raise_for_status()  # Raise an exception if the request was not successful

        data = response.json()  # Extract the JSON data from the response
        return data
    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected Error")


@router.get("/btc-price", summary="Fetch the current bitcoin to fiat price", response_model=PriceData)
def get_currencies(currency_code: str):

    try:
        response = requests.get(B_BTC_PRICE+"?currency="+currency_code.upper())
        response.raise_for_status()  # Raise an exception if the request was not successful

        data = response.json()  # Extract the JSON data from the response
        return data
    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected Error")
