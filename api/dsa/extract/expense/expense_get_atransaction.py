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
user_transaction = TransactionMessages(all_messages)


class GetATransaction:
    """This class extracts A transaction"""
    def __init__(self, transaction=user_transaction):
        self.transaction = transaction
    
    def get_a_transaction(self):
        """Extract transaction info using regex and convert dates to datetime objects"""
        sms_transaction = self.transaction.get_atransaction(messages=all_messages)
        
        # Receiver name
        beneficiary_name = [
            (re.search(r"by (.+?) on your MOMO account", sms).group(1).strip()
             if re.search(r"by (.+?) on your MOMO account", sms) else None)
            for sms in sms_transaction
        ]

        # Phone number
        beneficiary_phone_number = [
            (re.search(r"\((\d{12})\)", sms).group(1)
            if re.search(r"\((\d{12})\)", sms) else "Not Available")   
            for sms in sms_transaction
        ]

        # Amount
        amount = [
            float(re.search(r"transaction of (\d+(?:,\d{3})*) RWF", sms).group(1).replace(',', ''))
            if re.search(r"transaction of (\d+(?:,\d{3})*) RWF", sms) else None
            for sms in sms_transaction
        ]
        
        # Fee paid
        fee_paid = [
            float(re.search(r"Fee was (\d+(?:,\d{3})*) RWF", sms).group(1).replace(',', ''))
            if re.search(r"Fee was (\d+(?:,\d{3})*) RWF", sms) else None
            for sms in sms_transaction
        ]

        # Balance after
        balance_after = [
            int(re.search(r"New balance is (\d+(?:,\d{3})*) RWF", sms, re.IGNORECASE).group(1).replace(',', ''))
            if re.search(r"New balance is (\d+(?:,\d{3})*) RWF", sms, re.IGNORECASE) else None
            for sms in sms_transaction  
        ]

        # Currency
        currency = ["RWF" if "RWF" in sms else None for sms in sms_transaction] 

        # Transaction date
        transaction_date = [
            datetime.strptime(re.search(r"\b\d{4}-\d{2}-\d{2}\b", sms).group(0), "%Y-%m-%d")
            if re.search(r"\b\d{4}-\d{2}-\d{2}\b", sms) else None
            for sms in sms_transaction
        ]   

        # Transaction time
        transaction_time = [
            datetime.strptime(re.search(r"\b\d{2}:\d{2}:\d{2}\b", sms).group(0), "%H:%M:%S").time()
            if re.search(r"\b\d{2}:\d{2}:\d{2}\b", sms) else None
            for sms in sms_transaction
        ]

        # Combine date and time into one datetime
        transaction_datetime = [
            datetime.combine(d, t) if d and t else None
            for d, t in zip(transaction_date, transaction_time)
        ]

        tr_type = ["ATransaction"] * len(amount)

        return {
            "beneficiary_name": beneficiary_name,
            "beneficiary_phone_number": beneficiary_phone_number,
            "amount": amount,
            "fee_paid": fee_paid,
            "balance_after": balance_after,
            "currency": currency,
            "type": tr_type,
            "transaction_datetime": transaction_datetime
        }


if __name__ == "__main__":
    get_atransaction = GetATransaction(transaction=user_transaction)  
    result = get_atransaction.get_a_transaction()

    for key, value in result.items():
        print(f"{key}: {value}")
