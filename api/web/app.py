#!/usr/bin/env python3
import os
import json
import base64
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Imports from your project structure
from data.create_database.database import Transaction
from services.all_transaction import (
    get_transactions,
    get_transaction,
    get_transactions_summary,
    create_transaction,
    replace_transaction,
    delete_transaction,
)
from services.auth import Authentication

# Dynamically determine the database path relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.abspath(os.path.join(BASE_DIR, "../data/create_database/databases/momo.db"))

# Ensure database directory exists
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
print(DATABASE_PATH)
# SQLAlchemy setup
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
Session = sessionmaker(bind=engine)

# HTTP API Server
class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def _parse_id(self, path):
        """Extract ID from /transactions/{id}"""
        try:
            parts = path.strip("/").split("/")
            if len(parts) == 2 and parts[0] == "transactions":
                return int(parts[1])
        except:
            return None
        return None

    def _check_auth(self):
        """Basic auth check"""
        auth_header = self.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            return False, {"status": "Failed", "message": "Missing or invalid Authorization header"}

        encoded_credentials = auth_header.split(" ")[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode()
        try:
            email, password = decoded_credentials.split(":")
        except ValueError:
            return False, {"status": "Failed", "message": "Invalid Authorization format"}

        auth = Authentication({})
        result = auth.login({"email": email, "password_hash": password})
        if result.get("status") == "Login successful":
            return True, None
        return False, result

    
    # GET Endpoints
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/transactions":
            self._set_headers(200)
            self.wfile.write(json.dumps(get_transactions()).encode())
        elif path == "/transactions/summary":
            self._set_headers(200)
            self.wfile.write(json.dumps(get_transactions_summary()).encode())
        elif path.startswith("/transactions/") and path != "/transactions":
            tx_id = self._parse_id(path)
            if tx_id is None:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
                return
            response = get_transaction(tx_id)
            status = 200 if response.get("status") == "success" else 404
            self._set_headers(status)
            self.wfile.write(json.dumps(response).encode())

    # POST Endpoints
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        data = json.loads(body.decode()) if body else {}

        if path == "/transactions":
            response = create_transaction(data)
            self._set_headers(201 if response.get("status") == "Success" else 400)
            self.wfile.write(json.dumps(response).encode())
        elif path == "/signup":
            auth = Authentication(data)
            try:
                response = auth.signup()
                self._set_headers(201)
            except Exception as e:
                response = {"status": "Failed", "message": str(e)}
                self._set_headers(400)
            self.wfile.write(json.dumps(response).encode())
        elif path == "/login":
            auth = Authentication({})
            response = auth.login(data)
            self._set_headers(200 if response.get("status") == "Login successful" else 400)
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    # PUT /transactions/{id}
    def do_PUT(self):
        authorized, auth_response = self._check_auth()
        if not authorized:
            self._set_headers(401)
            self.wfile.write(json.dumps(auth_response).encode())
            return

        tx_id = self._parse_id(self.path)
        if tx_id is None:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        data = json.loads(body.decode())

        response = replace_transaction(tx_id, data)
        status = 200 if response.get("status") == "Success" else 404 if "not found" in response.get("message", "").lower() else 400
        self._set_headers(status)
        self.wfile.write(json.dumps(response).encode())

    # DELETE /transactions/{id}
    def do_DELETE(self):
        authorized, auth_response = self._check_auth()
        if not authorized:
            self._set_headers(401)
            self.wfile.write(json.dumps(auth_response).encode())
            return

        tx_id = self._parse_id(self.path)
        if tx_id is None:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
            return

        response = delete_transaction(tx_id)
        status = 200 if response.get("status") == "Success" else 404 if "not an int" in response.get("message", "").lower() else 400
        self._set_headers(status)
        self.wfile.write(json.dumps(response).encode())

# Run Serve
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
