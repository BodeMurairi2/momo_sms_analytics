Perfect! Here's a **modern, professional README** version for your project with badges, prerequisites, and example API requests:

---

# Momo SMS Analytics API

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

This project provides access to transaction data from the `momo.xml` file and allows you to manage transactions via a RESTful API.

---

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Running the Server](#running-the-server)
* [API Documentation](#api-documentation)
* [Database Initialization](#database-initialization)
* [Example API Requests](#example-api-requests)
* [Contact](#contact)
* [Contributing](#contributing)
* [Authors](#authors)

---

## Features

* Add, update, and delete mobile money transactions
* View transaction summaries
* API authentication with Basic Auth
* Fully documented API endpoints

---

## Prerequisites

* Python 3.10+
* pip
* Git

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/BodeMurairi2/momo_sms_analytics.git
```

2. **Navigate to the API directory**

```bash
cd momo_sms_analytics/api/
```

3. **Create and activate a virtual environment**

```bash
python3 -m venv venv
```

* **Linux / macOS:**

```bash
source venv/bin/activate
```

* **Windows (CMD / Git Bash):**

```bash
.\venv\Scripts\activate
# or
source venv/Scripts/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the Server

```bash
python3 -m web.app
```

The server will be accessible at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Detailed instructions for all endpoints are in:

```
docs/api_docs.md
```

* Signup
* Add a transaction
* Replace a transaction
* Delete a transaction
* Summary endpoints

---

## Database Initialization

If your database is empty or the browser does not display anything, inside api/ folder, run:

```bash
python3 -m data.create_database.create_database
python3 -m data.save_database.save_all_transaction
python3 -m data.save_database.save_income
python3 -m data.save_database.save_expense
```

---

## Example API Requests

### Signup

```bash
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Bode",
    "last_name": "Murairi",
    "phone_number": "250795020998",
    "email": "bodemurairi2@gmail.com",
    "password": "Bode200"
  }'
```

### Add a Transaction

```bash
curl -i -X POST http://localhost:8000/transactions \
  -u "bodemurairi2@gmail.com:Bode200" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "payment",
    "transaction_date": "2024-06-08 15:28",
    "amount": 2500
  }'
```

### Update a Transaction

```bash
curl -i -X PUT http://localhost:8000/transactions/5 \
  -u "bodemurairi2@gmail.com:Bode200" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "payment",
    "transaction_date": "2024-06-08 15:28",
    "amount": 2500
  }'
```

### Delete a Transaction

```bash
curl -i -X DELETE http://localhost:8000/transactions/5 \
  -u "bodemurairi2@gmail.com:Bode200"
```

### Get Transaction Summary

```bash
curl -i -X GET http://127.0.0.1:8000/transactions/summary \
  -u "bodemurairi2@gmail.com:Bode200"
```
```
  Path to the test script: api/services/test_transactions.py
```
---

## Contact

For any issues or questions:

* Pascal Louis Nsigo: [p.nsigo@alustudent.com](mailto:p.nsigo@alustudent.com)
* Maurice Nshimyumukiza: [m.nshimyumu@alustudent.com](mailto:m.nshimyumu@alustudent.com)
* Bode Murairi: [b.murairi@alustudent.com](mailto:b.murairi@alustudent.com)

---

## Contributing

Contributions, suggestions, and feedback are always welcome! Feel free to submit issues or pull requests.

---

## Authors

* Pascal Louis Nsigo: [p.nsigo@alustudent.com](mailto:p.nsigo@alustudent.com)
* Bode Murairi: [b.murairi@alustudent.com](mailto:b.murairi@alustudent.com)
* Maurice Nshimyumukiza: [m.nshimyumu@alustudent.com](mailto:m.nshimyumu@alustudent.com)

---
