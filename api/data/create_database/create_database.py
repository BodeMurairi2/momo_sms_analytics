#!/usr/bin/env python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.create_database.database import Base

# Database setup
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "databases", "momo.db")
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

# Drop all existing tables (optional safety: uncomment if you want a clean slate each run)
Base.metadata.drop_all(engine)

# Create all tables
Base.metadata.create_all(engine)

# Create a session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
