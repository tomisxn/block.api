# Block API

### Check Bitcoin Balance
'**GET /api/v1/bitcoin/balance/{address}**'

Get the current balance of a Bitcoin address.

#### Parameters

- '**address**' (string, required): The Bitcoin address for which you want to check the balance.

#### Response

```bash
{
  "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
  "balance": 0.01342158,
  "currency": "BTC"
}
```

### Get Bitcoin Transaction History
'**GET /api/v1/bitcoin/history/{address}**'

Get the transaction history of a Bitcoin address.

#### Parameters

- '**address**' (string, required): The Bitcoin address for which you want to get the transaction history.

#### Response

```bash
{
  "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
  "transactions": [
    {
      "txid": "2f2f816ff43e41e825ee5786d9df16a850fb15afab8c17d8881a0a524fccf72f",
      "amount": 0.00213543,
      "timestamp": 1678443285
    },
    {
      "txid": "4c6c0c8f80d42f3c8c28818cb8f0c8d58bf0a66efdb8b8f9d35a6e5b5a2dd12a",
      "amount": 0.00728615,
      "timestamp": 1678442991
    },
    // more transactions...
  ]
}
```

## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [API Documentation](#api-documentation)
- [Error Handling](#error-handling)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Installation

Brief instructions on how to install and set up your API.

```bash
# Example installation command
pip install my-api-package
```

### Usage

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
