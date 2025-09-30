#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
from datetime import datetime
from dsa.extract import TransactionMessages, get_messages

MOMO_DATA = ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")
all_messages = get_messages(data=MOMO_DATA)
user_transaction = TransactionMessages(messages=all_messages)

class GetWithdrawn:
    """This function get all transfer transaction data"""
    def __init__(self):
        self.withdrawn = user_transaction
    
    def get_withdrawn(self):
        """Get payment information"""
        all_withdrawn_transaction = self.withdrawn.get_withdrawn(messages=all_messages)
        
        # get withdrawn amount
        amount = [
            int(re.search(r"withdrawn\s+([\d,]+)\s*RWF", msg).group(1).replace(",", ""))
            for msg in all_withdrawn_transaction
        ]

        # Extract currency for withdrawn amount
        currency = ["RWF"]*len(amount)

        # beneficiary name
        beneficiary_name = [
            re.search(r"Agent\s+([A-Za-z ]+)\s+\(", msg).group(1).strip()
            for msg in all_withdrawn_transaction
        ]

        # beneficiary phone
        beneficiary_phone = [
            re.search(r"Agent [A-Za-z ]+ \((\d+)\)", msg).group(1)
            for msg in all_withdrawn_transaction
        ]

        # Extract transaction datetime
        transaction_datetime = [
            datetime.strptime(re.search(r"at\s+([\d-]+\s[\d:]+)", msg).group(1), "%Y-%m-%d %H:%M:%S")
            for msg in all_withdrawn_transaction
        ]

        # Extract new balance
        balance_after = [
            int(re.search(r"Your new balance:\s*([\d,]+)\s*RWF", msg).group(1).replace(",", ""))
            for msg in all_withdrawn_transaction
        ]

        # Extract fee paid
        fee_paid = [
            float(re.search(r"Fee paid:\s*([\d,]+)\s*RWF", msg).group(1).replace(",", ""))
            if re.search(r"Fee paid:\s*([\d,]+)\s*RWF", msg) else 0.0
            for msg in all_withdrawn_transaction
            ]

        transaction_type = ["Withdrawn"] * len(amount)
        return {
            "beneficiary_name": beneficiary_name,
            "beneficiary_phone": beneficiary_phone,
            "amount":amount,
            "fee_paid": fee_paid,
            "currency": currency,
            "type": transaction_type,
            "balance_after": balance_after,
            "transaction_datetime": transaction_datetime
        }

if __name__ == "__main__":
    get_withdrawn = GetWithdrawn()
    print(get_withdrawn.get_withdrawn())
