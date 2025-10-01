#!/usr/bin/env python3

"""This script loads all the transactions"""

from pathlib import Path
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from data.create_database.database import Transaction

# Dynamically determine the database path relative to this script
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "../data/create_database/databases/momo.db"

# Create database engine with absolute path
engine = create_engine(f"sqlite:///{DB_PATH.resolve()}")

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()


def classify_transaction(transaction: str) -> str:
    """Classify transaction as income or expense"""
    if transaction.lower() in ["receive", "deposit"]:
        return "Income"
    return "Expense"


def get_transactions():
    """Retrieve all transactions"""
    all_transaction = session.query(Transaction).all()
    response = [{"status": "success"}] + [
        {
            "id": transaction.transaction_id,
            "transaction_timestamp": f"{str(transaction.timestamp).split()[0]} {str(transaction.timestamp).split()[1][:5]}",
            "transaction": classify_transaction(transaction.type),
            "details": {
                "transaction_type": transaction.type,
                "amount": float(transaction.amount),
                "currency": "RWF",
                "transaction_date": f"On {str(transaction.transaction_date).split()[0]} at {str(transaction.transaction_date).split()[1][:5]}",
            },
        }
        for transaction in all_transaction
    ]
    return response

def get_transaction(transaction_id: int):
    """Return a specific transaction"""
    if not isinstance(transaction_id, int):
        return {
            "status": "Failed",
            "message": f"Transaction_id: {transaction_id} is not an Integer (eg. 5, 10, 20)"
        }

    transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()

    if not transaction:
        return {
            "status": "Failed",
            "message": f"Transaction {transaction_id} not found!"
        }

    return {
        "id": transaction.transaction_id,
        "transaction_timestamp": f"{str(transaction.timestamp).split()[0]} {str(transaction.timestamp).split()[1][:5]}",
        "transaction": classify_transaction(transaction.type),
        "details": {
            "transaction_type": transaction.type,
            "amount": float(transaction.amount),
            "currency": "RWF",
            "transaction_date": f"On {str(transaction.transaction_date).split()[0]} at {str(transaction.transaction_date).split()[1][:5]}",
        },
        "status": "success"
    }


def get_transactions_summary():
    """This function provides the summary/total of all transactions"""
    total_count = session.query(func.count(Transaction.transaction_id)).scalar()
    total_amount = session.query(func.sum(Transaction.amount)).scalar() or 0.0
    return {
        "total_transactions": total_count,
        "total_amount": total_amount,
        "currency": "RWF"
    }


def get_transactions_filter(type=None, min_amount=None, max_amount=None):
    """Filter transactions by type and/or amount"""
    q = session.query(Transaction)
    if type:
        q = q.filter(Transaction.type == type)
    if min_amount:
        q = q.filter(Transaction.amount >= float(min_amount))
    if max_amount:
        q = q.filter(Transaction.amount <= float(max_amount))

    return [{"status": "success"}] + [
        {
            "id": transaction.transaction_id,
            "transaction_timestamp": f"{str(transaction.timestamp).split()[0]} {str(transaction.timestamp).split()[1][:5]}",
            "transaction": classify_transaction(transaction.type),
            "details": {
                "transaction_type": transaction.type,
                "amount": float(transaction.amount),
                "currency": "RWF",
                "transaction_date": f"On {str(transaction.transaction_date).split()[0]} at {str(transaction.transaction_date).split()[1][:5]}",
            },
        }
        for transaction in q.all()
    ]


def get_transaction_limit(limit):
    """Get the most recent transactions limited by `limit`"""
    limit = int(limit)
    results = session.query(Transaction).all()[:limit]
    return [{"status": "success"}] + [
        {
            "id": transaction.transaction_id,
            "transaction_timestamp": f"{str(transaction.timestamp).split()[0]} {str(transaction.timestamp).split()[1][:5]}",
            "transaction": classify_transaction(transaction.type),
            "details": {
                "transaction_type": transaction.type,
                "amount": float(transaction.amount),
                "currency": "RWF",
                "transaction_date": f"On {str(transaction.transaction_date).split()[0]} at {str(transaction.transaction_date).split()[1][:5]}",
            },
        }
        for transaction in results
    ]


def create_transaction(data: dict):
    """Create a new transaction from a dictionary"""
    required_fields = ["type", "amount", "transaction_date"]
    missing_fields = [f for f in required_fields if f not in data]
    if missing_fields:
        return {
            "status": "Failed",
            "message": f"Missing required fields: {', '.join(missing_fields)}"
        }

    try:
        transaction_datetime = datetime.strptime(data["transaction_date"], "%Y-%m-%d %H:%M")
    except ValueError:
        return {
            "status": "Failed",
            "message": "transaction_date must be in 'YYYY-MM-DD HH:MM' format"
        }

    transaction = Transaction(
        type=data["type"],
        amount=float(data["amount"]),
        transaction_date=transaction_datetime
    )

    try:
        session.add(transaction)
        session.commit()
        return {
            "status": "Success",
            "message": "Transaction added successfully",
            "record": {
                "id": transaction.transaction_id,
                "transaction": classify_transaction(transaction.type),
                "transaction_type": transaction.type,
                "amount": transaction.amount,
                "currency": "RWF",
                "transaction_date": f"{transaction.transaction_date.date()} at {transaction.transaction_date.strftime('%H:%M')}"
            }
        }
    except SQLAlchemyError as e:
        session.rollback()
        return {
            "status": "Failed",
            "message": f"Database error: {str(e)}"
        }


def replace_transaction(transaction_id: int, data: dict):
    """Replace a transaction completely"""
    if not isinstance(transaction_id, int):
        return {
            "status": "Failed",
            "message": f"{transaction_id} is not an integer. Use examples like 5, 10, 20."
        }

    transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
    if not transaction:
        return {
            "status": "Failed",
            "message": f"Transaction with ID {transaction_id} not found."
        }

    required_fields = ["type", "amount", "transaction_date"]
    missing_fields = [f for f in required_fields if f not in data]
    if missing_fields:
        return {
            "status": "Failed",
            "message": f"Missing required fields: {', '.join(missing_fields)}"
        }

    try:
        transaction_datetime = datetime.strptime(data["transaction_date"], "%Y-%m-%d %H:%M")
    except ValueError:
        return {
            "status": "Failed",
            "message": "transaction_date must be in 'YYYY-MM-DD HH:MM' format"
        }

    transaction.type = data["type"]
    transaction.amount = float(data["amount"])
    transaction.transaction_date = transaction_datetime

    try:
        session.commit()
        return {
            "status": "Success",
            "message": f"Transaction {transaction_id} replaced successfully",
            "record": {
                "id": transaction.transaction_id,
                "transaction": classify_transaction(transaction.type),
                "transaction_type": transaction.type,
                "amount": transaction.amount,
                "currency": "RWF",
                "transaction_date": f"{transaction.transaction_date.date()} at {transaction.transaction_date.strftime('%H:%M')}"
            }
        }
    except SQLAlchemyError as e:
        session.rollback()
        return {
            "status": "Failed",
            "message": f"Database error: {str(e)}"
        }


def delete_transaction(transaction_id: int):
    """Delete a transaction"""
    if not isinstance(transaction_id, int):
        return {"status": "Failed",
                "message": f"Impossible to delete a transaction. Id:{transaction_id} not an int (eg. 2, 5, 10)."}

    transaction = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
    if not transaction:
        return {"status": "Failed",
                "message": f"Transaction {transaction_id} not found."}

    session.delete(transaction)
    session.commit()
    return {"status": "Success",
            "message": f"Record {transaction_id} deleted successfully"}


if __name__ == "__main__":
    print(get_transactions_summary())
