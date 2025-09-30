#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET
from datetime import datetime
from dsa.extract import TransactionMessages, get_messages

class GetPayment:
    '''This class extract payment transaction'''
    def __init__(self, transaction):
        self.transaction = transaction
    
    def get_payment(self):
        '''Extract transaction info using'''
        sms_transaction = self.transaction.get_payment(messages=all_messages)

        # Beneficiary name
        beneficiary_name = [
            re.search(r"\b[A-Z][a-z]+(?:\s[A-Z]\.?)?\s[A-Z][a-z]+\b", sms) or
            re.search(r"to\s+(.+?)(?:\s+\(\d{9,12}\)|\s+with token)", sms)
            if re.search(r"to\s+(.+?)(?:\s+\(\d{9,12}\)|\s+with token)", sms) or re.search(r"\b[A-Z][a-z]+(?:\s[A-Z]\.?)?\s[A-Z][a-z]+\b", sms)
            else None
            for sms in sms_transaction
        ]

        # Phone number (keep original regex)
        beneficiary_phone_number = [
            (re.search(r"to\s+[A-Za-z]+\s+[A-Za-z]+\s+(\d{5})", sms).group(1)
            if re.search(r"to\s+[A-Za-z]+\s+[A-Za-z]+\s+(\d{5})", sms) else "Not Available")   
            for sms in sms_transaction
        ]

        # Amount
        amount = [
            float(re.search(r"Your payment of\s*([0-9,]+)\s*RWF", sms).group(1).replace(',', ''))
            if re.search(r"Your payment of\s*([0-9,]+)\s*RWF", sms) else None
            for sms in sms_transaction
        ]

        # Fee paid
        fee_paid = [
            float(re.search(r"to\s+[A-Za-z]+\s+[A-Za-z]+\s+(\d{5})", sms).group(1).replace(',', ''))
            if re.search(r"to\s+[A-Za-z]+\s+[A-Za-z]+\s+(\d{5})", sms) else 0.0
            for sms in sms_transaction
        ]

        # Balance after
        balance_after = [
            int(re.search(r"Your new balance:\s*([0-9,]+)", sms, re.IGNORECASE).group(1).replace(',', ''))
            if re.search(r"Your new balance:\s*([0-9,]+)", sms, re.IGNORECASE) else None
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

        return {
            "beneficiary_name": beneficiary_name,
            "beneficiary_phone_number": beneficiary_phone_number,
            "amount": amount,
            "fee_paid": fee_paid,
            "balance_after": balance_after,
            "currency": currency,
            "transaction_date": transaction_date,
            "transaction_time": transaction_time
        }
if __name__ == "__main__":
    all_messages = get_messages(data=ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")) 
    user_transaction = TransactionMessages(all_messages)
    get_transfer = GetPayment(transaction=user_transaction)
    print(get_transfer.get_payment())
