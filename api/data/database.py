#!/usr/bin/env python3

from sqlalchemy import (
    Column, Integer, String, Float, Boolean,
    DateTime, Date
)
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timezone, UTC

Base = declarative_base()

class Client(Base):
    """This table stores all enrolled user information"""
    __tablename__ = "Clients"
    user_id = Column(Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(500), nullable=False)

class Transaction(Base):
    """
    "This table stores all the transaction"
    """
    __tablename__ = "All_Transaction"
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    transaction_date = Column(DateTime)
    transaction_time = Column(DateTime)

class Expenses(Base):
    ''' This table stores all the transactions that are expenses'''
    __tablename__ = "Expenses"
    transaction_id = Column(Integer, primary=True, autoincremnent=True)
    beneficiary_name = Column(String(100), nullable=False)
    beneficiary_phone_number = Column(String)
    amount = Column(Float, nullable=False)
    fee_paid = Column(Float, nullable=False)
    balance_after = Column(Float,nullable=False)
    currency = Column(String(50), default="RWF")
    transaction_date = Column(DateTime)
    transaction_time = Column(DateTime)

class Income(Base):
    """This table stores all transactions that are incomes"""
    __tablename__ = "Income"
    transaction_id = Column(Integer, primary=True, autoincrement=True)
    sender_name = Column(String(100), nullable = False)
    sender_phone_number = Column(String(100), nullable = False)
    amount = Column(float, nullable=False )
    balance_after = Column(float, nullable=False)
    currency = Column(String(50), default="RWF")
    transction_date = Column(DateTime)
    timestamp = Column(DateTime, default=datetime.utcnow)
    transaction_time = Column(DateTime)
