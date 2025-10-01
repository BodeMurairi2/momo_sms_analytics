#!/usr/bin/env python3

"""This script handles authentication"""

import base64
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.create_database.database import Client

# Dynamically determine the database path relative to this script
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "../data/create_database/databases/momo.db"

# Create database engine with absolute path
engine = create_engine(f"sqlite:///{DB_PATH.resolve()}")

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()


class Authentication:
    """Basic Authentication"""

    def __init__(self, user_info: dict):
        self.user_data = user_info

    def signup(self):
        """Signup a new user"""
        password_hash = base64.b64encode(self.user_data["password_hash"].encode()).decode()
        new_user = Client(
            first_name=self.user_data["first_name"],
            last_name=self.user_data["last_name"],
            phone_number=self.user_data["phone_number"],
            email=self.user_data["email"],
            password_hash=password_hash
        )
        session.add(new_user)
        session.commit()

        return {
            "status": "Successful",
            "message": f"Welcome: {self.user_data['first_name']} {self.user_data['last_name']}"
        }

    def login(self, data: dict):
        """Login a user"""
        find_user = session.query(Client).filter(Client.email == data["email"]).first()
        if not find_user:
            return {
                "status": "Failed",
                "message": "User not found"
            }

        if base64.b64encode(data["password_hash"].encode()).decode() == find_user.password_hash:
            return {
                "status": "Login successful",
                "message": f"Welcome Back {find_user.first_name} {find_user.last_name}"
            }
        else:
            return {
                "status": "Failed",
                "message": "Incorrect password"
            }


if __name__ == "__main__":
    auth = Authentication({
        "first_name": "Bode",
        "last_name": "Murairi",
        "phone_number": "250788123456",
        "email": "bode@example.com",
        "password_hash": "mypassword123"
    })
    print(auth.signup())
    print(auth.login({"email": "bode@example.com", "password_hash": "mypassword123"}))
