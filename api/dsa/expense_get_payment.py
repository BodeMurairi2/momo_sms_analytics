#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
from datetime import datetime
from dsa.extract import TransactionMessages, get_messages

all_messages = get_messages(data=ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")) 
user_transaction = TransactionMessages(all_messages)

class GetPayment:
    """This class extracts payment transaction information"""
    def __init__(self):
        self.transaction = user_transaction
    
    def get_payment(self):
        """Extract transaction info using regex"""
        sms_transaction = self.transaction.get_payment(messages=all_messages)

        # Beneficiary name
        beneficiary_name = [
            (re.search(r"\b[A-Z][a-z]+(?:\s[A-Z]\.?)?\s[A-Z][a-z]+\b", sms).group(0)
            if re.search(r"\b[A-Z][a-z]+(?:\s[A-Z]\.?)?\s[A-Z][a-z]+\b", sms)
            else re.search(r"to\s+(.+?)(?:\s+\d{5}|\s+with token)", sms).group(1).strip()
            if re.search(r"to\s+(.+?)(?:\s+\d{5}|\s+with token)", sms) else "Not Available")
            for sms in sms_transaction
        ]

        # Phone number (5-digit code)
        beneficiary_phone_number = [
            re.search(r"to\s+[A-Za-z]+\s+[A-Za-z]+\s+(\d{5})", sms).group(1)
            if re.search(r"to\s+[A-Za-z]+\s+[A-Za-z]+\s+(\d{5})", sms) else "Not Available"
            for sms in sms_transaction
        ]

        # Amount
        amount = [
            float(re.search(r"Your payment of\s*([\d,]+)\s*RWF", sms).group(1).replace(',', ''))
            if re.search(r"Your payment of\s*([\d,]+)\s*RWF", sms) else None
            for sms in sms_transaction
        ]

        # Fee paid
        fee_paid = [
            float(re.search(r"Fee (?:was|paid)[:\s]*([\d,]+)\s*RWF", sms).group(1).replace(',', ''))
            if re.search(r"Fee (?:was|paid)[:\s]*([\d,]+)\s*RWF", sms) else 0.0
            for sms in sms_transaction
        ]

        # Balance after
        balance_after = [
            int(re.search(r"Your new balance[:\s]*([\d,]+)\s*RWF", sms, re.IGNORECASE).group(1).replace(',', ''))
            if re.search(r"Your new balance[:\s]*([\d,]+)\s*RWF", sms, re.IGNORECASE) else None
            for sms in sms_transaction
        ]

        # Currency
        currency = ["RWF" if "RWF" in sms else None for sms in sms_transaction] 

        # Transaction datetime (combine date and time)
        transaction_datetime = [
            datetime.strptime(
                f"{re.search(r'(\d{4}-\d{2}-\d{2})', sms).group(1)} {re.search(r'(\d{2}:\d{2}:\d{2})', sms).group(1)}",
                "%Y-%m-%d %H:%M:%S"
            )
            if re.search(r'(\d{4}-\d{2}-\d{2})', sms) and re.search(r'(\d{2}:\d{2}:\d{2})', sms)
            else None
            for sms in sms_transaction
        ]

        tr_type = ["Payment"] * len(amount)

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
    get_payment = GetPayment(transaction=user_transaction)
    print(get_payment.get_payment())
