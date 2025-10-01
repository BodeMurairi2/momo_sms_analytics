#!/usr/bin/env python3

import requests


# Transaction data to update
transaction_data = {
    "type": "payment",
    "transaction_date": "2024-06-08 15:28",
    "amount": 2500
}

# Authentication credentials
email = "b.murairi@alustudent.com"
password = "bode200"

try:
    # Send PUT request to /transactions/{id} with Basic Auth
    response = requests.post(
        url=f"http://localhost:8000/transactions/{transaction_id=5}",
        json=transaction_data,
        auth=(email, password),
        timeout=30
    )

    print("Status code:", response.status_code)
    print("Response:", response.json())

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
