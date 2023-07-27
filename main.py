# main.py
# Import your API route(s) from the routes directory
from app.routes import bitcoin
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware  # CORS (Cross-Origin Resource Sharing) middleware
from fastapi import FastAPI, Request, HTTPException
# Import config
from app.config import *

description = """
## API Description
- Bitcoin Balance:
    - Users can retrieve the current balance of a specific Bitcoin address by making a GET request to the
    **/api/v1/bitcoin/balance/{address}** endpoint. The response includes the address, balance, and currency (BTC).

- Bitcoin Transaction History:
    -  Users can obtain the transaction history of a Bitcoin address by sending a GET request to 
    **/api/v1/bitcoin/history/{address}**. The API responds with a list of transactions made to and from the given address, 
    including transaction IDs (txids), amounts, and timestamps.

- Bitcoin Transaction Details:
    -  Users can fetch detailed information about a particular Bitcoin transaction using the 
    **/api/v1/bitcoin/transaction/{txid}** endpoint. The response provides transaction-specific data such as the transaction
     ID (txid), amount, timestamp, confirmations, inputs (with previous transaction details), and outputs.
"""

app = FastAPI(
    title="Block 🛸",
    version="v1.0",
    description=description,
    contact={
        "name": "Tomisin Owolabi",
        "url": "https://github.com/tomisxn",
        "email": "oluwatomisin.owolabi@yahoo.com",
    },
    debug=DEBUG,
)

# Include the API route(s) using the router from the imported file(s)
app.include_router(bitcoin.router, prefix=API_PREFIX+"/bitcoin", tags=["Bitcoin"])  # Example with a prefix

# Optional: Set up additional configurations and middleware here
origins = ["http://localhost", "http://localhost:3000"]  # Replace with your frontend's origin(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Redirect to /docs
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


# Custom exception handler for "Internal Server Error"
@app.middleware("http")
async def catch_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": "Internal Server Error"},
        )


# Optional: Add startup and shutdown events
@app.on_event("startup")
async def startup_event():
    # Code to run on application startup
    pass


@app.on_event("shutdown")
async def shutdown_event():
    # Code to run on application shutdown
    pass
