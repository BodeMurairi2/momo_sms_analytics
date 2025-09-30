#!/usr/bin/env python3

"""Extract all transactions"""
import re
import xml.etree.ElementTree as ET
from typing import Any, Dict, List

MOMO_XML = ET.parse(
    "/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml"
)

def get_messages(xml_data):
    """Get all SMS messages from the XML file"""
    sms_nodes = xml_data.findall("sms")
    if not sms_nodes:
        return []
    return [node.attrib["body"] for node in sms_nodes]

all_messages = get_messages(xml_data=MOMO_XML)

class AllTransactions:
    """Extract all transactions"""
    def __init__(self):
        """Initialize with all SMS messages"""
        self.all_messages = all_messages
    
    def get_all_data(self) -> Dict[str, List[Any]]:
        """Return all transactions as a dictionary of lists"""
        transactions_dict = {
            "amount": [],
            "transaction_type": [],
            "transaction_datetime": []
        }

        # Regex patterns for extracting fields
        amount_regex = re.compile(r"(\d{1,3}(?:,\d{3})*|\d+)\s*RWF")
        datetime_regex = re.compile(r"at\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})")

        for message in self.all_messages:
            # Extract amount
            amount_match = amount_regex.search(message)
            amount_value = amount_match.group(1).replace(",", "") if amount_match else None

            # Extract datetime
            datetime_match = datetime_regex.search(message)
            transaction_datetime = datetime_match.group(1) if datetime_match else None

            # Identify transaction type
            if "received" in message.lower():
                transaction_type = "receive"
            elif "payment" in message.lower():
                transaction_type = "payment"
            elif "deposit" in message.lower():
                transaction_type = "deposit"
            elif "withdrawn" in message.lower() or "withdraw" in message.lower():
                transaction_type = "withdrawal"
            elif "transferred" in message.lower() or "transfer" in message.lower():
                transaction_type = "transfer"
            else:
                transaction_type = "other"

            # Only add valid transactions
            if amount_value and transaction_datetime:
                transactions_dict["amount"].append(int(amount_value))
                transactions_dict["transaction_type"].append(transaction_type)
                transactions_dict["transaction_datetime"].append(transaction_datetime)

        return transactions_dict


if __name__ == "__main__":
    transaction_extractor = AllTransactions()
    transaction_data = transaction_extractor.get_all_data()
    print(transaction_data)
