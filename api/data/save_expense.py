#!/usr/bin/env python3

"""This script saves to the database"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.database import Expenses
from dsa.expense_get_withdrawn import GetWithdrawn
from dsa.expense_get_umaze_kugura import GetUmazeKugura
from dsa.expense_get_atransaction import GetATransaction
from dsa.expense_get_transfer import GetTransfer
from dsa.expense_get_payment import GetPayment

# Create database engine
db_path = Path(__file__).resolve().parent / "databases/momo.db"
engine = create_engine(f"sqlite:///{db_path}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

class SaveExpense:
    """Class to save information to the database"""
    def __init__(self, expense_data):
        self.expense_data = expense_data
    
    def save_expense(self):
        """Save all expense records to the database"""
        for name, phone, amount, fee_paid, balance_after, currency, tr_type, tr_datetime in zip(
            self.expense_data["beneficiary_name"],
            self.expense_data["beneficiary_phone_number"],   # standardized
            self.expense_data["amount"],
            self.expense_data["fee_paid"],
            self.expense_data["balance_after"],
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

class SaveGetWithdrawn(SaveExpense):
    """Save withdrawn"""
    def __init__(self):
        withdrawn_data = GetWithdrawn().get_withdrawn()
        super().__init__(withdrawn_data)

class SaveGetUmaze(SaveExpense):
    """Save Umaze Kugura"""
    def __init__(self):
        umaze_data = GetUmazeKugura().get_umaze_kugura()
        super().__init__(umaze_data)

class SaveGetAtransaction(SaveExpense):
    """Save a transaction"""
    def __init__(self):
        a_transaction = GetATransaction().get_a_transaction()
        super().__init__(a_transaction)

class SaveGetTransfer(SaveExpense):
    """Save a transfer"""
    def __init__(self):
        transfer_data = GetTransfer().get_transfer()
        super().__init__(transfer_data)

class SaveGetPayment(SaveExpense):
    """Save a payment"""
    def __init__(self):
        payment_data = GetPayment().get_payment()
        super().__init__(payment_data)


if __name__ == "__main__":
    SaveGetWithdrawn().save_expense()
    SaveGetUmaze().save_expense()
    SaveGetAtransaction().save_expense()
    SaveGetTransfer().save_expense()
    SaveGetPayment().save_expense()
    
    session.close()
