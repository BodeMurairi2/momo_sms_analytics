#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from dsa.extract.extract import TransactionMessages, get_messages

# Dynamically determine the path to momo.xml relative to this script
BASE_DIR = Path(__file__).resolve().parent
MOMO_DATA_PATH = BASE_DIR / "momo.xml"
MOMO_DATA = ET.parse(MOMO_DATA_PATH)

all_messages = get_messages(data=MOMO_DATA)
user_transaction = TransactionMessages(messages=all_messages)


class GetWithdrawn:
    """This class gets all transfer transaction data"""
    def __init__(self):
        self.withdrawn = user_transaction
    
    def get_withdrawn(self):
        """Get withdrawn transaction information"""
        all_withdrawn_transaction = self.withdrawn.get_withdrawn(messages=all_messages)
        
        # Withdrawn amount
        amount = [
            int(re.search(r"withdrawn\s+([\d,]+)\s*RWF", msg).group(1).replace(",", ""))
            for msg in all_withdrawn_transaction
        ]

        currency = ["RWF"] * len(amount)

        # Beneficiary name
        beneficiary_name = [
            re.search(r"Agent\s+([A-Za-z ]+)\s+\(", msg).group(1).strip()
            for msg in all_withdrawn_transaction
        ]

        # Beneficiary phone
        beneficiary_phone = [
            re.search(r"Agent [A-Za-z ]+ \((\d+)\)", msg).group(1)
            for msg in all_withdrawn_transaction
        ]

        # Transaction datetime
        transaction_datetime = [
            datetime.strptime(re.search(r"at\s+([\d-]+\s[\d:]+)", msg).group(1), "%Y-%m-%d %H:%M:%S")
            for msg in all_withdrawn_transaction
        ]

        # New balance
        balance_after = [
            int(re.search(r"Your new balance:\s*([\d,]+)\s*RWF", msg).group(1).replace(",", ""))
            for msg in all_withdrawn_transaction
        ]

        # Fee paid
        fee_paid = [
            float(re.search(r"Fee paid:\s*([\d,]+)\s*RWF", msg).group(1).replace(",", ""))
            if re.search(r"Fee paid:\s*([\d,]+)\s*RWF", msg) else 0.0
            for msg in all_withdrawn_transaction
        ]

        transaction_type = ["Withdrawn"] * len(amount)

        return {
            "beneficiary_name": beneficiary_name,
            "beneficiary_phone_number": beneficiary_phone,
            "amount": amount,
            "fee_paid": fee_paid,
            "balance_after": balance_after,
            "currency": currency,
            "type": transaction_type,
            "transaction_datetime": transaction_datetime
        }


if __name__ == "__main__":
    get_withdrawn = GetWithdrawn()
    print(get_withdrawn.get_withdrawn())
