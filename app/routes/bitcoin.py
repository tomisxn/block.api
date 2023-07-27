# app/routes/bitcoin.py
import json
import requests
from fastapi import APIRouter, HTTPException
from app.models.bitcoin import Balance
from app.schemas.bitcoin import BalanceDataResponse

router = APIRouter()


@router.post("/balance", summary="Returns balance and unconfirmed amount(Amount waiting 2 confirmations) of multiple "
                                 "addresses/xpubs", response_model=BalanceDataResponse)
def get_balance(payload: Balance):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer L36Et14WBZhruA0NIJ9GQSQoNwsGqgs4OQXYkhn7GXA'
    }
    data = json.dumps({
        "addr": payload.addr,
    })

    try:
        response = requests.post("https://www.blockonomics.co/api/balance", headers=headers, data=data)
        response.raise_for_status()  # Raise an exception if the request was not successful

        data = response.json()  # Extract the JSON data from the response
        return data
    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Request Error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected Error")


@router.post("/history", summary="Returns transaction history of multiple bitcoin addresses/xpubs", response_model=BalanceDataResponse)
def get_balance(payload: Balance):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer L36Et14WBZhruA0NIJ9GQSQoNwsGqgs4OQXYkhn7GXA'
    }
    data = json.dumps({
        "addr": payload.addr,
    })

    try:
        response = requests.post("https://www.blockonomics.co/api/balance", headers=headers, data=data)
        response.raise_for_status()  # Raise an exception if the request was not successful

        data = response.json()  # Extract the JSON data from the response
        return data
    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Request Error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected Error")
