#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
from dsa.extract import TransactionMessages, get_messages
from datetime import datetime

MOMO_DATA = ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")
all_messages = get_messages(data=MOMO_DATA)
user_transaction = TransactionMessages(messages=all_messages)

class GetBankIncome:
    """This class gets bank transaction income"""

    def __init__(self):
        self.transaction = user_transaction

    def get_bank_income(self):
        """Extract transaction info and combine date/time into one datetime column"""

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

        # transaction datetime (combine date + time)
        transaction_datetime = [
            datetime.strptime(
                f"{date_match.group(1)} {time_match.group(1)}", "%Y-%m-%d %H:%M:%S"
            )
            for sms in sms_transaction
            if (
                (date_match := re.search(r"(\d{4}-\d{2}-\d{2})", sms))
                and (time_match := re.search(r"(\d{2}:\d{2}:\d{2})", sms))
            )
        ]

        type = ["Bank Transfer"] * len(currency)

        return {
            "sender_name": sender_name,
            "phone_number": phone_number,
            "amount": amount,
            "currency": currency,
            "balance_after": balance_after,
            "transaction_datetime": transaction_datetime,
            "type": type
        }

if __name__ == "__main__":
    bank_income = GetBankIncome()
    print(bank_income.get_bank_income())
