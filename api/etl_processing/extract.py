#!/usr/bin/env python3

""""
This script extract messages from xml files
"""

import xml.etree.ElementTree as ET
import re
from typing import Any

momo_data = ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")

def get_messages(data):
    """This function get all messages"""
    all_data = data.findall("sms")
    if not all_data:
        return []
    return [node.attrib["body"] for node in all_data]

class TransactionMessages:
    """ this class retrieves all Momo transaction sms and categorizes them"""
    def __init__(self, messages:Any):
        self.__all_messages = messages

    def check_messages(self, messages)->list[str]:
        """This function check if message is available"""
        if not messages:
            return None
        self.__all_messages = messages
        return self.__all_messages

    def get_momo_income(self, messages) -> list[str]:
        """this function get all income messages momo to momo"""
        if not self.check_messages(messages):
            return []
        return [message for message in self.__all_messages if message.startswith("You have received")]

    def get_bank_income(self, messages)-> list[str]:
        """This function get all income messages from bank"""
        if not self.check_messages(messages):
            return []
        return [message for message in self.__all_messages if message.startswith("*113*R*A bank deposit of")]

    def get_payment(self, messages) -> list[str]:
        """Get all your payment messages"""
        if not self.check_messages(messages):
            return []
        return [message for message in self.__all_messages if re.search(r"Your payment of", message, re.I)]

    def get_transfer(self, messages)-> list[str]:
        """this function get all transferred to messages"""
        if not self.check_messages(messages):
            return []
        return [message for message in self.__all_messages if re.search(r"transferred to", message, re.I)]

    def get_withdrawn(self, messages) -> list[str]:
        """ get all widthdrawn messages"""
        if not self.check_messages(messages):
            return []
        return [message for message in self.__all_messages if re.findall(pattern="withdrawn", string=message, flags=re.I)]

    def get_atransaction(self, messages) -> list[str]:
        """Get all A transaction messages"""
        if not self.check_messages(messages):
            return []
        return [message for message in self.__all_messages if re.findall(pattern="A transaction", string=message, flags=re.I)]

    def get_umaze(self, messges) -> list[str]:
        """Get all umaze messages"""
        if not self.check_messages(messges):
            return []
        return [message for message in self.__all_messages if re.search("Umaze kugura", message, re.I)]

    def get_total_messages(self):
        """get the number of total messages"""
        return f"Total Messages: {len(self.__all_messages)}"
