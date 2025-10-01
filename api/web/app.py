#!/usr/bin/env python3
import os
import json
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from data.database import Transaction
from services.all_transaction import (
    get_transactions,
    get_transaction,
    create_transaction,
    replace_transaction,
    delete_transaction,
    get_transactions_summary,
    get_transactions_filter,
    get_transaction_limit
)

# Database Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = os.path.join(BASE_DIR, "../data/databases/momo.db")
engine = create_engine(f"sqlite:///{os.path.abspath(DATABASE_URL)}")
Session = sessionmaker(bind=engine)


# API Server
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

    # GET Endpoints
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        # GET /transactions list all
        if path == "/transactions":
            self._set_headers(200)
            self.wfile.write(json.dumps(get_transactions()).encode())

        # GET /transactions/{id}
        elif path.startswith("/transactions/") and path != "/transactions":
            tx_id = self._parse_id(path)
            if tx_id is None:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
                return

            response = get_transaction(tx_id)
            if response.get("status") == "success":
                self._set_headers(200)
            else:
                self._set_headers(404)
            self.wfile.write(json.dumps(response).encode())

        # GET /transactions/summary
        elif path == "/transactions/summary":
            self._set_headers(200)
            self.wfile.write(json.dumps(get_transactions_summary()).encode())

    # POST /transactions
    def do_POST(self):
        if self.path != "/transactions":
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())
            return

        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        data = json.loads(body.decode())

        response = create_transaction(data)

        if response["status"] == "Success":
            self._set_headers(201)
        else:
            self._set_headers(400)

        self.wfile.write(json.dumps(response).encode())

    # PUT /transactions/{id}
    def do_PUT(self):
        tx_id = self._parse_id(self.path)
        if tx_id is None:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
            return

        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        data = json.loads(body.decode())

        response = replace_transaction(tx_id, data)

        if response["status"] == "Success":
            self._set_headers(200)
        else:
            self._set_headers(400 if "not found" not in response.get("message", "").lower() else 404)

        self.wfile.write(json.dumps(response).encode())

    # DELETE /transactions/{id}
    def do_DELETE(self):
        tx_id = self._parse_id(self.path)
        if tx_id is None:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
            return

        response = delete_transaction(tx_id)

        if response["status"] == "Success":
            self._set_headers(200)
        else:
            self._set_headers(400 if "not an int" in response.get("message", "").lower() else 404)

        self.wfile.write(json.dumps(response).encode())


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://127.0.0.1:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
