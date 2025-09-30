#!/usr/bin/env bash

"""This script saves to the database"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.database import Expenses
from dsa.get_withdrawn import GetWithdrawn
from dsa.umaze_kugura import GetUmazeKugura
from dsa.expense_get_atransaction import GetATransaction
from dsa.expense_get_transfer import GetTransfer
from dsa.expense_get_payment import GetPayment

# Create database engine
db_path = Path(__file__).resolve().parent / "databases/momo.db"
engine = create_engine(f'sqlite:///{db_path}')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

class SaveExpense:
    """Class to save information to the database"""
    def __init__(self, expense_class):
        self.expense_data = expense_class
    
    def save_expense(self):
        """Save all expense records to the database"""
        for name, phone, amount, fee_paid, balance_after, currency, tr_type, tr_datetime in zip(
            self.expense_data["beneficiary_name"],
            self.expense_data["beneficiary_phone"],
            self.expense_data["amount"],
            self.expense_data["fee_paid"],
            self.expense_data["balance_after"]
            self.expense_data["currency"],
            self.expense_data["type"],
            self.expense_data["transaction_datetime"]
        ):
            new_record = Expenses(
                beneficiary_name=name,
                beneficiary_phone_number=phone,
                amount=amount,
                fee_paid=fee_paid,
                balance_after=balance_after,
                currency=currency,
                type=tr_type,
                transaction_date=tr_datetime
            ) 
            session.add(new_record)
        session.commit()
        session.close()

class SaveGetWithdrawn(SaveExpense):
    """Save withdrawn"""
    def __init__(self):
        withdrawn_data = GetWithdrawn()
        super().__init__(self, withdrawn_data.get_withdrawn())

class SaveGetUmaze(SaveExpense):
    """Save Umaze Kugura"""
    def __init__(self):
        umaze_kugura = GetUmazeKugura()
        super().__init__(self, umaze_kugura.umaze_kugura())

class SaveGetAtransaction(SaveExpense):
    """Save a transaction"""
    def __init__(self):
        a_transaction = GetATransaction()
        super().__init__(self, a_transaction.get_a_transaction())

class SaveGetTransfer(SaveExpense):
    """Save a transfer"""
    def __init__(self):
        a_transfer = GetTransfer()
        super().__init__(self, a_transfer.get_transfer())

class SaveGetPayment(SaveExpense):
    """Save a payment"""
    def __init__(self):
        get_payment = GetPayment()
        super().__init__(get_payment.get_payment())
