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


class GetUmazeKugura:
    """This class collects expenses information from Umaze Kugura"""
    def __init__(self):
        self.umaze_kugura = user_transaction.get_umaze(messages=all_messages)

    def get_umaze_kugura(self):
        """Get all Umaze Kugura expenses messages"""
        amount = [
            float(re.search(r"igura\s+(\d{1,3}(?:,\d{3})*|\d+)\s*RWF", msg, re.IGNORECASE).group(1).replace(",", ""))
            for msg in self.umaze_kugura
            if re.search(r"igura\s+(\d{1,3}(?:,\d{3})*|\d+)\s*RWF", msg, re.IGNORECASE)
        ]

        beneficiary_name = ["Umaze Kugura"] * len(amount)
        beneficiary_phone = ["Unknown"] * len(amount)
        fee_paid = [0] * len(amount)
        balance_after = [0] * len(amount)
        tr_type = ["Data Bundles"] * len(amount)
        currency = ["RWF"] * len(amount)

        # Example static datetime for all transactions
        transaction_datetime = [
            datetime.strptime("12-05-2025 16:25", "%d-%m-%Y %H:%M")
        ] * len(amount)

        return {
            "beneficiary_name": beneficiary_name,
            "beneficiary_phone_number": beneficiary_phone,
            "amount": amount,
            "fee_paid": fee_paid,
            "balance_after": balance_after,
            "currency": currency,
            "type": tr_type,
            "transaction_datetime": transaction_datetime
        }


if __name__ == "__main__":
    umaze = GetUmazeKugura()
    print(umaze.get_umaze_kugura())
