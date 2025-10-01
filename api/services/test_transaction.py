#!/usr/bin/env python3

"""This script implements linear search and dictionary lookup with execution time measurement"""

import time

# Sample transaction data (50 records)
transactions_data = [
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1001, "transaction": "Expense", "transaction_type": "payment", "amount": 2350.0, "currency": "RWF", "transaction_date": "2023-07-15 at 14:12"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1002, "transaction": "Income", "transaction_type": "deposit", "amount": 10250.5, "currency": "RWF", "transaction_date": "2024-02-03 at 09:45"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1003, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 7500.0, "currency": "RWF", "transaction_date": "2023-11-20 at 16:30"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1004, "transaction": "Expense", "transaction_type": "transfer", "amount": 15000.0, "currency": "RWF", "transaction_date": "2024-05-12 at 12:10"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1005, "transaction": "Income", "transaction_type": "receive", "amount": 5000.0, "currency": "RWF", "transaction_date": "2024-08-18 at 18:55"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1006, "transaction": "Expense", "transaction_type": "payment", "amount": 3200.0, "currency": "RWF", "transaction_date": "2023-03-29 at 11:05"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1007, "transaction": "Income", "transaction_type": "deposit", "amount": 24000.0, "currency": "RWF", "transaction_date": "2024-10-05 at 08:40"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1008, "transaction": "Expense", "transaction_type": "airtime", "amount": 1200.0, "currency": "RWF", "transaction_date": "2023-06-12 at 19:25"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1009, "transaction": "Income", "transaction_type": "receive", "amount": 8750.0, "currency": "RWF", "transaction_date": "2024-01-23 at 14:50"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1010, "transaction": "Expense", "transaction_type": "payment", "amount": 4100.0, "currency": "RWF", "transaction_date": "2023-12-07 at 17:15"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1011, "transaction": "Expense", "transaction_type": "transfer", "amount": 6700.0, "currency": "RWF", "transaction_date": "2023-08-14 at 10:05"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1012, "transaction": "Income", "transaction_type": "deposit", "amount": 18500.0, "currency": "RWF", "transaction_date": "2024-03-01 at 09:30"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1013, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 2500.0, "currency": "RWF", "transaction_date": "2023-05-20 at 16:45"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1014, "transaction": "Income", "transaction_type": "receive", "amount": 7200.0, "currency": "RWF", "transaction_date": "2024-07-11 at 12:20"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1015, "transaction": "Expense", "transaction_type": "payment", "amount": 9800.0, "currency": "RWF", "transaction_date": "2023-09-02 at 15:40"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1016, "transaction": "Income", "transaction_type": "deposit", "amount": 13500.0, "currency": "RWF", "transaction_date": "2024-04-18 at 11:15"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1017, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 4500.0, "currency": "RWF", "transaction_date": "2023-01-25 at 18:00"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1018, "transaction": "Income", "transaction_type": "receive", "amount": 9000.0, "currency": "RWF", "transaction_date": "2024-06-05 at 13:30"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1019, "transaction": "Expense", "transaction_type": "transfer", "amount": 5600.0, "currency": "RWF", "transaction_date": "2023-10-21 at 10:55"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1020, "transaction": "Income", "transaction_type": "deposit", "amount": 14250.0, "currency": "RWF", "transaction_date": "2024-09-09 at 08:50"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1021, "transaction": "Expense", "transaction_type": "payment", "amount": 3100.0, "currency": "RWF", "transaction_date": "2023-04-08 at 17:20"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1022, "transaction": "Income", "transaction_type": "receive", "amount": 11200.0, "currency": "RWF", "transaction_date": "2024-02-27 at 14:10"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1023, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 4200.0, "currency": "RWF", "transaction_date": "2023-07-30 at 09:35"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1024, "transaction": "Income", "transaction_type": "deposit", "amount": 19250.0, "currency": "RWF", "transaction_date": "2024-08-22 at 16:40"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1025, "transaction": "Expense", "transaction_type": "transfer", "amount": 6700.0, "currency": "RWF", "transaction_date": "2023-12-12 at 11:25"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1026, "transaction": "Income", "transaction_type": "receive", "amount": 8050.0, "currency": "RWF", "transaction_date": "2024-03-15 at 13:55"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1027, "transaction": "Expense", "transaction_type": "payment", "amount": 2900.0, "currency": "RWF", "transaction_date": "2023-09-19 at 15:10"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1028, "transaction": "Income", "transaction_type": "deposit", "amount": 12750.0, "currency": "RWF", "transaction_date": "2024-05-07 at 10:45"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1029, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 3600.0, "currency": "RWF", "transaction_date": "2023-03-18 at 18:20"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1030, "transaction": "Income", "transaction_type": "receive", "amount": 9650.0, "currency": "RWF", "transaction_date": "2024-01-12 at 09:55"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1031, "transaction": "Expense", "transaction_type": "transfer", "amount": 5150.0, "currency": "RWF", "transaction_date": "2023-05-25 at 11:40"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1032, "transaction": "Income", "transaction_type": "deposit", "amount": 20300.0, "currency": "RWF", "transaction_date": "2024-06-28 at 14:25"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1033, "transaction": "Expense", "transaction_type": "payment", "amount": 4800.0, "currency": "RWF", "transaction_date": "2023-08-09 at 17:50"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1034, "transaction": "Income", "transaction_type": "receive", "amount": 7500.0, "currency": "RWF", "transaction_date": "2024-04-16 at 12:15"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1035, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 3900.0, "currency": "RWF", "transaction_date": "2023-10-02 at 16:30"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1036, "transaction": "Income", "transaction_type": "deposit", "amount": 14250.0, "currency": "RWF", "transaction_date": "2024-07-20 at 09:50"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1037, "transaction": "Expense", "transaction_type": "payment", "amount": 5200.0, "currency": "RWF", "transaction_date": "2023-06-15 at 11:20"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1038, "transaction": "Income", "transaction_type": "receive", "amount": 8800.0, "currency": "RWF", "transaction_date": "2024-02-08 at 15:05"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1039, "transaction": "Expense", "transaction_type": "transfer", "amount": 6100.0, "currency": "RWF", "transaction_date": "2023-09-27 at 10:50"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1040, "transaction": "Income", "transaction_type": "deposit", "amount": 19750.0, "currency": "RWF", "transaction_date": "2024-08-30 at 08:40"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1041, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 4500.0, "currency": "RWF", "transaction_date": "2023-03-11 at 13:15"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1042, "transaction": "Income", "transaction_type": "receive", "amount": 11200.0, "currency": "RWF", "transaction_date": "2024-01-28 at 12:40"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1043, "transaction": "Expense", "transaction_type": "payment", "amount": 3900.0, "currency": "RWF", "transaction_date": "2023-07-04 at 16:05"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1044, "transaction": "Income", "transaction_type": "deposit", "amount": 15250.0, "currency": "RWF", "transaction_date": "2024-05-19 at 10:20"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1045, "transaction": "Expense", "transaction_type": "transfer", "amount": 6700.0, "currency": "RWF", "transaction_date": "2023-12-30 at 11:55"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1046, "transaction": "Income", "transaction_type": "receive", "amount": 9400.0, "currency": "RWF", "transaction_date": "2024-06-02 at 14:10"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1047, "transaction": "Expense", "transaction_type": "withdrawal", "amount": 3600.0, "currency": "RWF", "transaction_date": "2023-02-22 at 17:40"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1048, "transaction": "Income", "transaction_type": "deposit", "amount": 18250.0, "currency": "RWF", "transaction_date": "2024-03-23 at 09:55"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1049, "transaction": "Expense", "transaction_type": "payment", "amount": 4100.0, "currency": "RWF", "transaction_date": "2023-09-14 at 15:35"}},
    {"status": "Success", "message": "Transaction added successfully", "record": {"id": 1050, "transaction": "Income", "transaction_type": "receive", "amount": 10200.0, "currency": "RWF", "transaction_date": "2024-07-25 at 13:20"}}
]

# Convert list to dictionary for fast lookup: id -> transaction
transactions_by_id = {transaction["record"]["id"]: transaction for transaction in transactions_data}

def search_linear(transaction_list, transaction_id):
    """Search for a transaction by ID using linear search"""
    for transaction in transaction_list:
        if transaction["record"]["id"] == transaction_id:
            return transaction
    return None

def search_dictionary(transaction_dict, transaction_id):
    """Search for a transaction by ID using dictionary lookup"""
    return transaction_dict.get(transaction_id)

if __name__ == "__main__":
    sample_ids_to_test = [1005, 1020, 1035, 1040, 1050] 

    for transaction_id in sample_ids_to_test:
        # Linear search
        start_time = time.time()
        linear_result = search_linear(transactions_data, transaction_id)
        end_time = time.time()
        print(f"Linear search for ID {transaction_id}: {linear_result}")
        print(f"Linear search time: {end_time - start_time:.8f} seconds\n")

        # Dictionary lookup
        start_time = time.time()
        dictionary_result = search_dictionary(transactions_by_id, transaction_id)
        end_time = time.time()
        print(f"Dictionary lookup for ID {transaction_id}: {dictionary_result}")
        print(f"Dictionary lookup time: {end_time - start_time:.8f} seconds\n")
