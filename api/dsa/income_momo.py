#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
from datetime import datetime
from dsa.extract import TransactionMessages, get_messages

class GetMomoIncome:
    """This class extract momo to momo transaction"""
    def __init__(self, transaction):
        self.transaction = transaction
    
    def get_income_momo(self):
        """Extract transaction info using regex and convert dates to datetime objects"""
        sms_transaction = self.transaction.get_momo_income(messages=all_messages)
        
        # Sender name
        sender_name = [
            (re.search(r"from\s+([A-Za-z'\- ]+)\s*\(", sms).group(1).strip()
             if re.search(r"from\s+([A-Za-z'\- ]+)\s*\(", sms) else None)
            for sms in sms_transaction
        ]

        # Phone number (keep original regex)
        phone_number = [
            (re.search(r"\((\*+\d+)\)", sms).group(1)
             if re.search(r"\((\*+\d+)\)", sms) else None)
            for sms in sms_transaction
        ]

        # Amount
        amount = [
            float(re.search(r"You have received\s+([\d,]+)\s+RWF", sms).group(1).replace(',', ''))
            if re.search(r"You have received\s+([\d,]+)\s+RWF", sms) else None
            for sms in sms_transaction
            ]

        # Balance after
        balance_after = [
            int(re.search(r"new balance:\s*([\d,]+)\s*RWF", sms, re.IGNORECASE).group(1).replace(',', ''))
            if re.search(r"new balance:\s*([\d,]+)\s*RWF", sms, re.IGNORECASE) else None
            for sms in sms_transaction
        ]

        # Currency
        currency = ["RWF" if "RWF" in sms else None for sms in sms_transaction]
        
        # Transaction date
        transaction_date = [
            datetime.strptime(
                re.search(r"at\s+(\d{4}-\d{2}-\d{2})\s+\d{2}:\d{2}:\d{2}", sms).group(1),
                "%Y-%m-%d"
                ).date()
                if re.search(r"at\s+(\d{4}-\d{2}-\d{2})\s+\d{2}:\d{2}:\d{2}", sms) else None
                for sms in sms_transaction
                ]

        # Transaction time
        transaction_time = [
            datetime.strptime(
                re.search(r"at\s+\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})", sms).group(1),
                "%H:%M:%S"
                ).time()
                if re.search(r"at\s+\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})", sms) else None
                for sms in sms_transaction
                ]

        return {
            "sender_name": sender_name,
            "phone_number": phone_number,
            "amount": amount,
            "balance_after": balance_after,
            "currency": currency,
            "transaction_date": transaction_date,
            "transaction_time": transaction_time
        }
if __name__ == "__main__":
    get_momo_income = GetMomoIncome(transaction=user_transaction)
