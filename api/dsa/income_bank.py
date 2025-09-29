#!/usr/bin/env bash

import re
import xml.etree.ElementTree as ET
from dsa.extract import TransactionMessages, get_messages
from datetime import datetime

class GetBankIncome:
    """This class get momo transaction income """

    def __init__(self, transaction):
        self.transaction = transaction

    def get_bank_income(self):
        """Extract transaction info using regex and keep date/time separate"""

        sms_transaction = self.transaction.get_bank_income(messages=all_messages)

        # amount
        amount = [
            int(match.group(1))
            for sms in sms_transaction
            if (match := re.search(r"A bank deposit of (\d+)", sms))
        ]

        # currency
        currency = [
            match.group(1)
            for sms in sms_transaction
            if (match := re.search(r"A bank deposit of \d+ (\w+)", sms))
        ]

        # sender name
        sender_name = ["Bank Deposit"] * len(currency)

        # phone number
        phone_number = ["*113*R*A"] * len(currency)

        # balance after
        balance_after = [
            int(match.group(1))
            for sms in sms_transaction
            if (match := re.search(r"Your NEW BALANCE\s*:(\d+) \w+", sms))
        ]

        # transaction date
        transaction_date = [
            match.group(1)
            for sms in sms_transaction
            if (match := re.search(r"(\d{4}-\d{2}-\d{2})", sms))
        ]

        # transaction time
        transaction_time = [
            match.group(1)
            for sms in sms_transaction
            if (match := re.search(r"(\d{2}:\d{2}:\d{2})", sms))
        ]

        return {
            "sender_name": sender_name,
            "sender_phone_number": phone_number,
            "amount": amount,
            "currency": currency,
            "balance_after": balance_after,
            "transaction_date": transaction_date,
            "transaction_time": transaction_time
        }

if __name__ == "__main__":
    bank_income = GetBankIncome(transaction=user_transaction)
