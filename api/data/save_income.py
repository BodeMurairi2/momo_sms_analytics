#!/usr/bin/env python3

"""
This script handles saving all income to the database
"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.database import Income
from dsa.income_momo import GetMomoIncome
from dsa.income_bank import GetBankIncome

# Create database engine
db_path = Path(__file__).resolve().parent / "databases/momo.db"
engine = create_engine(f'sqlite:///{db_path}')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


class SaveIncome:
    """class to save income information to the database"""

    def __init__(self, income_class):
        """
        income_class: dictionary containing parsed transaction data
        """
        self.income_class = income_class

    def save_income(self):
        """Save all income records to the database"""
        for name, phone, amount, balance, currency, tr_datetime, tr_type in zip(
            self.income_class["sender_name"],
            self.income_class["phone_number"],
            self.income_class["amount"],
            self.income_class["balance_after"],
            self.income_class["currency"],
            self.income_class["transaction_datetime"],
            self.income_class["type"]
        ):
            record = Income(
                sender_name=name,
                sender_phone_number=phone,
                amount=amount,
                balance_after=balance,
                currency=currency,
                transaction_date=tr_datetime,
                type=tr_type
            )
            session.add(record)

        session.commit()
        session.close()


class SaveIncomeMomo(SaveIncome):
    """Save Momo Income"""
    def __init__(self):
        momo_income = GetMomoIncome()
        super().__init__(momo_income.get_income_momo())


class SaveIncomeBank(SaveIncome):
    """Save Bank income"""
    def __init__(self):
        bank_income = GetBankIncome()
        super().__init__(bank_income.get_bank_income())


save_momo = SaveIncomeMomo()
save_bank = SaveIncomeBank()

save_momo.save_income()
save_bank.save_income()
