#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
from datetime import datetime
from dsa.extract import TransactionMessages, get_messages

all_messages = get_messages(data=ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")) 
user_transaction = TransactionMessages(all_messages)

class GetTransfer:
    """This class extracts Momo-to-Momo transaction information"""
    def __init__(self):
        self.transaction = user_transaction
    
    def get_transfer(self):
        """Extract transaction info using regex and convert dates to datetime objects"""
        sms_transaction = self.transaction.get_transfer(messages=all_messages)

        # Receiver name (first and last name)
        beneficiary_name = [
            re.search(r"\b[A-Z][a-z]+(?:\s[A-Z]\.?)?\s[A-Z][a-z]+\b", sms).group(0)
            if re.search(r"\b[A-Z][a-z]+(?:\s[A-Z]\.?)?\s[A-Z][a-z]+\b", sms)
            else "Not Available"
            for sms in sms_transaction
        ]

        # Phone number (12 digits)
        beneficiary_phone_number = [
            re.search(r"\((\d{12})\)", sms).group(1)
            if re.search(r"\((\d{12})\)", sms) else None
            for sms in sms_transaction
        ]

        # Amount
        amount = [
            float(re.search(r"(\d+(?:,\d+)*)\s*RWF", sms).group(1).replace(',', ''))
            if re.search(r"(\d+(?:,\d+)*)\s*RWF", sms) else None
            for sms in sms_transaction
        ]

        # Fee paid
        fee_paid = [
            float(re.search(r"Fee was[:\s]*([\d,]+)\s*RWF", sms).group(1).replace(',', ''))
            if re.search(r"Fee was[:\s]*([\d,]+)\s*RWF", sms) else 0.0
            for sms in sms_transaction
        ]

        # Balance after
        balance_after = [
            int(re.search(r"New balance[:\s]*([\d,]+)\s*RWF", sms, re.IGNORECASE).group(1).replace(',', ''))
            if re.search(r"New balance[:\s]*([\d,]+)\s*RWF", sms, re.IGNORECASE) else None
            for sms in sms_transaction
        ]

        # Currency
        currency = ["RWF" if "RWF" in sms else None for sms in sms_transaction]

        # Transaction datetime (combined date and time)
        transaction_datetime = [
            datetime.strptime(
                f"{re.search(r'(\d{4}-\d{2}-\d{2})', sms).group(1)} {re.search(r'(\d{2}:\d{2}:\d{2})', sms).group(1)}",
                "%Y-%m-%d %H:%M:%S"
            )
            if re.search(r'(\d{4}-\d{2}-\d{2})', sms) and re.search(r'(\d{2}:\d{2}:\d{2})', sms)
            else None
            for sms in sms_transaction
        ]
        tr_type = ["Transfer"] * len(transaction_datetime)

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
    all_messages = get_messages(data=ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")) 
    user_transaction = TransactionMessages(all_messages)

    get_transfer = GetTransfer(transaction=user_transaction)
    transfer_data = get_transfer.get_transfer()
    print(transfer_data)
