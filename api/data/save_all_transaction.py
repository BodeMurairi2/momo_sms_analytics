#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.database import Transaction
from dsa.extract_all_transaction import AllTransactions

# Create database engine
db_path = Path(__file__).resolve().parent / "databases/momo.db"
engine = create_engine(f"sqlite:///{db_path}")

# Create a session factory
Session = sessionmaker(bind=engine)


class SaveAllTransaction:
    def __init__(self):
        self.all_transaction = AllTransactions()
    
    def save_all_transaction(self):
        """Save all transactions"""
        all_transaction = self.all_transaction.get_all_data()

        with Session() as session:
            for amount, transaction_type, transaction_datetime in zip(
                all_transaction["amount"],
                all_transaction["transaction_type"],
                all_transaction["transaction_datetime"]
            ):
                # Convert datetime string -> Python datetime object
                transaction_datetime_obj = datetime.strptime(
                    transaction_datetime, "%Y-%m-%d %H:%M:%S"
                )

                new_record = Transaction(
                    type=transaction_type,
                    amount=amount,
                    transaction_date=transaction_datetime_obj
                )
                session.add(new_record)

            session.commit()


if __name__ == "__main__":
    saver = SaveAllTransaction()
    saver.save_all_transaction()
    print("All transactions saved successfully!")
