#!/usr/bin/env python3

import requests

# Transaction data to send
transaction_id = 20

try:
    # Send PUT request to /transactions/{id}
    response = requests.delete(
        url=f"http://localhost:8000/transactions/{transaction_id}",
        timeout=30
    )

    print("Status code:", response.status_code)
    print("Response:", response.json())

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
