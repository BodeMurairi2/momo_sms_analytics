Absolutely! Here’s a **well-formatted, structured, and readable API documentation** version of your content:

---

# Momo SMS Analytics API Documentation

Explore the full project on GitHub: [https://github.com/BodeMurairi2/momo_sms_analytics.git](https://github.com/BodeMurairi2/momo_sms_analytics.git)

---

## 1. GET `/transactions`

**Description:** Retrieve all transactions.

**Request Example:**

```http
GET /transactions
```

**Response Example:**

```http
HTTP/1.0 200 OK
Content-Type: application/json

[
  {
    "status": "success"
  },
  {
    "id": 1,
    "transaction_timestamp": "2025-10-01 16:32",
    "transaction": "Income",
    "details": {
      "transaction_type": "receive",
      "amount": 2000.0,
      "currency": "RWF",
      "transaction_date": "On 2024-05-10 at 16:30"
    }
  },
  {
    "id": 2,
    "transaction_timestamp": "2025-10-01 16:32",
    "transaction": "Expense",
    "details": {
      "transaction_type": "payment",
      "amount": 1000.0,
      "currency": "RWF",
      "transaction_date": "On 2024-05-10 at 16:31"
    }
  }
]
```
---

## 2. GET `/transactions/{id}`

**Description:** Get details of a specific transaction by ID.

**Request Example:**

```http
GET /transactions/2
```

**Response Example:**

```http
HTTP/1.0 200 OK
Content-Type: application/json

{
  "id": 5,
  "transaction_timestamp": "2025-10-01 16:32",
  "transaction": "Expense",
  "details": {
    "transaction_type": "payment",
    "amount": 2000.0,
    "currency": "RWF",
    "transaction_date": "On 2024-05-11 at 18:48"
  },
  "status": "success"
}
```
---

## 3. POST `/signup`

**Description:** Sign up to the platform.

**Request Example:**

```bash
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "max",
    "last_name": "charles",
    "phone_number": "250795020998",
    "email": "b.murairi2@gmail.com",
    "password_hash": "bode200"
  }'
```

**Response Example:**

```json
{"status": "Successful", "message": "Welcome: max charles"}
```
---

## 4. POST `/transactions`

**Description:** Create a new transaction.

> Note: You must be registered and logged in to create a transaction.

**Request Example:**

```bash
curl -i -X POST http://localhost:8000/transactions \
  -u "b.murairi@alustudent.com:bode200" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "payment",
    "transaction_date": "2024-06-08 15:28",
    "amount": 2500
  }'
```

**Response Example:**

```http
HTTP/1.0 201 Created
Content-Type: application/json

{
  "status": "Success",
  "message": "Transaction added successfully",
  "record": {
    "id": 1661,
    "transaction": "Expense",
    "transaction_type": "payment",
    "amount": 2500.0,
    "currency": "RWF",
    "transaction_date": "2024-06-08 at 15:28"
  }
}
```

**Error Codes:**

* `422` – Missing required fields
* `400` – Bad request
* `401` – Unauthorized

---

## 5. PUT `/transactions/{id}`

**Description:** Update an existing transaction.

> Note: PUT completely replaces the transaction. Registration and authentication are required.

**Request Example:**

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

**Response Example:**

```http
HTTP/1.0 200 OK
Content-Type: application/json

{
  "status": "Success",
  "message": "Transaction 5 replaced successfully",
  "record": {
    "id": 5,
    "transaction": "Expense",
    "transaction_type": "payment",
    "amount": 2500.0,
    "currency": "RWF",
    "transaction_date": "2024-06-08 at 15:28"
  }
}
```

**Error Codes:**

* `422` – Missing required fields
* `400` – Bad request
* `401` – Unauthorized

---

## 6. DELETE `/transactions/{id}`

**Description:** Delete a transaction by ID.

> Registration and authentication required.

**Request Example:**

```bash
curl -i -X DELETE http://localhost:8000/transactions/5 \
  -u "bodemurairi2@gmail.com:Bode200"
```

**Response Example:**

```http
HTTP/1.0 200 OK
Content-Type: application/json

{"status": "Success", "message": "Record 5 deleted successfully"}
```

**Error Codes:**

* `204` – No Content
* `400` – Invalid ID format
* `404` – Transaction not found
* `401` – Unauthorized

---

## 7. GET `/transactions/summary`

**Description:** Retrieve a summary of all transactions (total count and total amount).

**Request Example:**

```http
GET http://127.0.0.1:8000/transactions/summary
```

**Response Example:**

```json
{
  "total_transactions": 1660,
  "total_amount": 32904496.0,
  "currency": "RWF"
}
```
---

## 8. Error Code Summary

| Code | Meaning                              |
| ---- | ------------------------------------ |
| 200  | OK – Success                         |
| 201  | Created – New transaction added      |
| 204  | No Content – Successful delete       |
| 400  | Bad Request – Invalid input or ID    |
| 401  | Unauthorized – Authentication failed |
| 404  | Not Found – Transaction not found    |
| 422  | Missing required fields              |

---
