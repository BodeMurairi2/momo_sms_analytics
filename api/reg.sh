#!/usr/bin/env bash
curl -v -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "dirac",
    "last_name": "murai",
    "phone_number": "250795020998",
    "email": "b.murairi@gmail.com",
    "password": "Bode2000"
  }'
