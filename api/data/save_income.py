#!/usr/bin/env python3

"""
This script handles saving all income to the database
"""
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dsa.income_momo import GetMomoIncome
from dsa.income_bank import GetBankIncome
from dsa.extract import TransactionMessages, get_messages

# Parse Momo messages
momo_data = ET.parse("/home/bode-murairi/Documents/programming/ALU/momo_sms_analytics/api/data/momo.xml")
all_messages = get_messages(data=momo_data)
user_transaction = TransactionMessages(messages=all_messages)

# Create database engine
engine = create_engine('sqlite:///databases/momo.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

class SaveIncome:
    """Generic class to save income information to the database"""

    def __init__(self, income_class, transaction):
        """
        income_class: ORM class (GetMomoIncome, GetBankIncome, etc.)
        transaction: TransactionMessages object containing parsed data
        """
        self.income_class = income_class
        self.transaction = transaction

    def save_income(self):
        """Save all income records to the database"""
        for name, phone, amount, balance, currency, tr_date, tr_time in zip(
            self.transaction["sender_name"],
            self.transaction["phone_number"],
            self.transaction["amount"],
            self.transaction["balance_after"],
            self.transaction["currency"],
            self.transaction["transaction_date"],
            self.transaction["transaction_time"]
        ):
            record = self.income_class(
                sender_name=name,
                sender_phone=phone,
                amount=amount,
                balance_after=balance,
                currency=currency,
                transaction_date=tr_date,
                transaction_time=tr_time
            )
            session.add(record)

        session.commit()
        session.close()

class SaveIncomeMomo(SaveIncome):
    """Save momo Income"""
    def __init__(self, transaction):
        super().__init__(GetMomoIncome, transaction)


class SaveIncomeBank(SaveIncome):
    """Save bank income"""
    def __init__(self, transaction):
        super().__init__(GetBankIncome, transaction)


# Save income
save_momo = SaveIncomeMomo(user_transaction)
save_bank = SaveIncomeBank(user_transaction)

save_momo.save_income()
save_bank.save_income()
