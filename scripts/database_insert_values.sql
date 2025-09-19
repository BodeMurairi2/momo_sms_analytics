-- =========================
-- CUSTOMERS (5 users)
-- =========================
INSERT INTO customers (first_name, last_name, phone_number, email, password_hash) VALUES
('John', 'Doe', '250700111111', 'john.doe@example.com', 'hash1'),
('Jane', 'Smith', '250700222222', 'jane.smith@example.com', 'hash2'),
('Michael', 'Brown', '250700333333', 'michael.brown@example.com', 'hash3'),
('Emily', 'Johnson', '250700444444', 'emily.johnson@example.com', 'hash4'),
('David', 'Wilson', '250700555555', 'david.wilson@example.com', 'hash5');

-- =========================
-- TRANSACTION CATEGORY (5 per user = 25 total)
-- =========================
INSERT INTO transaction_category (customer_id, transaction_type) VALUES
(1, 'Food'), (1, 'Transport'), (1, 'Bills'), (1, 'Shopping'), (1, 'Health'),
(2, 'Food'), (2, 'Transport'), (2, 'Savings'), (2, 'Entertainment'), (2, 'Bills'),
(3, 'Food'), (3, 'Transport'), (3, 'Shopping'), (3, 'Health'), (3, 'Bills'),
(4, 'Food'), (4, 'Entertainment'), (4, 'Shopping'), (4, 'Health'), (4, 'Bills'),
(5, 'Food'), (5, 'Savings'), (5, 'Transport'), (5, 'Bills'), (5, 'Entertainment');

-- =========================
-- SAVINGS ACCOUNT (5 per user = 25 total)
-- =========================
INSERT INTO savings_account (customer_id, balance, currency, description) VALUES
(1, 1500.50, 'USD', 'Emergency Fund'),
(1, 500.00, 'USD', 'Holiday Savings'),
(1, 200.00, 'USD', 'Transport Money'),
(1, 800.00, 'USD', 'Shopping Pot'),
(1, 1000.00, 'USD', 'Medical Savings'),

(2, 250.75, 'USD', 'Transport Savings'),
(2, 1500.00, 'USD', 'House Rent'),
(2, 2000.00, 'USD', 'Emergency Fund'),
(2, 700.00, 'USD', 'Fun Money'),
(2, 100.00, 'USD', 'Pocket Change'),

(3, 3200.00, 'USD', 'Utility Savings'),
(3, 800.00, 'USD', 'Holiday Trip'),
(3, 600.00, 'USD', 'Shopping Budget'),
(3, 1000.00, 'USD', 'Transport'),
(3, 400.00, 'USD', 'Phone Bills'),

(4, 500.00, 'USD', 'Fun Money'),
(4, 300.00, 'USD', 'Clothes'),
(4, 250.00, 'USD', 'Transport Fund'),
(4, 100.00, 'USD', 'Snacks'),
(4, 2000.00, 'USD', 'Long-term'),

(5, 10000.00, 'USD', 'Long-term Savings'),
(5, 500.00, 'USD', 'Gifts'),
(5, 200.00, 'USD', 'Transport'),
(5, 400.00, 'USD', 'Movies'),
(5, 600.00, 'USD', 'Short Trips');

-- =========================
-- SMS (5 per user = 25 total)
-- =========================
INSERT INTO sms (customer_id, address, date_sent, type, service_center, body) VALUES
(1, 'MTN Rwanda', '2025-09-01 10:15:00', 'Debit', 'MTN Center', 'You spent $20 on food.'),
(1, 'MTN Rwanda', '2025-09-02 12:30:00', 'Debit', 'MTN Center', 'Transport fee $5 deducted.'),
(1, 'MTN Rwanda', '2025-09-03 08:45:00', 'Credit', 'MTN Center', 'You received $50 refund.'),
(1, 'MTN Rwanda', '2025-09-04 09:20:00', 'Debit', 'MTN Center', 'Bills paid: $100.'),
(1, 'MTN Rwanda', '2025-09-05 19:00:00', 'Credit', 'MTN Center', 'Salary received $500.'),

(2, 'Airtel Rwanda', '2025-09-01 11:00:00', 'Debit', 'Airtel Center', 'Food purchase $15.'),
(2, 'Airtel Rwanda', '2025-09-02 14:00:00', 'Debit', 'Airtel Center', 'Transport fee $8 deducted.'),
(2, 'Airtel Rwanda', '2025-09-03 10:20:00', 'Credit', 'Airtel Center', 'Gift received $20.'),
(2, 'Airtel Rwanda', '2025-09-04 16:45:00', 'Debit', 'Airtel Center', 'Entertainment: $30.'),
(2, 'Airtel Rwanda', '2025-09-05 18:10:00', 'Credit', 'Airtel Center', 'Salary received $600.'),

(3, 'MTN Rwanda', '2025-09-01 09:15:00', 'Debit', 'MTN Center', 'Electricity bill $40.'),
(3, 'MTN Rwanda', '2025-09-02 15:00:00', 'Debit', 'MTN Center', 'Water bill $10.'),
(3, 'MTN Rwanda', '2025-09-03 18:25:00', 'Credit', 'MTN Center', 'Refund $30.'),
(3, 'MTN Rwanda', '2025-09-04 20:30:00', 'Debit', 'MTN Center', 'Internet $50.'),
(3, 'MTN Rwanda', '2025-09-05 11:40:00', 'Credit', 'MTN Center', 'Bonus payment $200.'),

(4, 'Airtel Rwanda', '2025-09-01 08:20:00', 'Debit', 'Airtel Center', 'Cinema tickets $15.'),
(4, 'Airtel Rwanda', '2025-09-02 13:10:00', 'Debit', 'Airtel Center', 'Shopping $40.'),
(4, 'Airtel Rwanda', '2025-09-03 17:30:00', 'Credit', 'Airtel Center', 'Friend sent $20.'),
(4, 'Airtel Rwanda', '2025-09-04 19:00:00', 'Debit', 'Airtel Center', 'Transport $7.'),
(4, 'Airtel Rwanda', '2025-09-05 21:45:00', 'Credit', 'Airtel Center', 'Salary $450.'),

(5, 'MTN Rwanda', '2025-09-01 07:00:00', 'Debit', 'MTN Center', 'Fuel purchase $60.'),
(5, 'MTN Rwanda', '2025-09-02 14:50:00', 'Debit', 'MTN Center', 'Groceries $35.'),
(5, 'MTN Rwanda', '2025-09-03 11:25:00', 'Credit', 'MTN Center', 'Gift $100.'),
(5, 'MTN Rwanda', '2025-09-04 18:00:00', 'Debit', 'MTN Center', 'Electricity $20.'),
(5, 'MTN Rwanda', '2025-09-05 10:00:00', 'Credit', 'MTN Center', 'Salary $800.');

-- =========================
-- EXPENSE (5 per user = 25 total)
-- =========================
INSERT INTO expense (sms_id, customer_id, transaction_type, beneficiary_name, beneficiary_phone_number, transaction_date, amount, fee_paid, balance_after, currency) VALUES
(1, 1, 'Food', 'Kigali Supermarket', '250781111111', '2025-09-01 10:15:00', 20.00, 0.50, 1480.00, 'USD'),
(2, 1, 'Transport', 'Motor Taxi', '250782222222', '2025-09-02 12:30:00', 5.00, 0.10, 1475.00, 'USD'),
(4, 1, 'Bills', 'REG Utility', '250783333333', '2025-09-04 09:20:00', 100.00, 1.00, 1375.00, 'USD'),
(5, 1, 'Shopping', 'City Market', '250784444444', '2025-09-05 19:00:00', 50.00, 0.50, 1325.00, 'USD'),
(2, 1, 'Health', 'Pharmacy Kigali', '250785555555', '2025-09-02 14:00:00', 25.00, 0.20, 1300.00, 'USD'),

(6, 2, 'Food', 'Restaurant Kigali', '250786111111', '2025-09-01 11:00:00', 15.00, 0.20, 235.55, 'USD'),
(7, 2, 'Transport', 'Bus Company', '250786222222', '2025-09-02 14:00:00', 8.00, 0.10, 227.45, 'USD'),
(9, 2, 'Entertainment', 'Century Cinema', '250786333333', '2025-09-03 10:20:00', 30.00, 0.25, 197.20, 'USD'),
(10, 2, 'Bills', 'WATER Utility', '250786444444', '2025-09-04 16:45:00', 20.00, 0.20, 177.00, 'USD'),
(6, 2, 'Savings', 'Equity Bank', '250786555555', '2025-09-01 18:00:00', 50.00, 0.50, 127.00, 'USD');

-- (continue same structure for customers 3, 4, 5 …)

-- =========================
-- INCOME (5 per user = 25 total)
-- =========================
INSERT INTO income (sms_id, customer_id, transaction_type, sender_name, sender_phone_number, transaction_date, amount, fee_paid, balance_after, currency) VALUES
(3, 1, 'Refund', 'Supermarket', '250781111111', '2025-09-03 08:45:00', 50.00, 0.50, 1350.00, 'USD'),
(5, 1, 'Salary', 'Company Ltd', '250799999999', '2025-09-05 19:00:00', 500.00, 2.00, 1850.00, 'USD'),
(3, 1, 'Bonus', 'Boss', '250700111111', '2025-09-03 14:00:00', 100.00, 0.50, 1950.00, 'USD'),
(5, 1, 'Gift', 'Friend Paul', '250700222222', '2025-09-05 20:00:00', 70.00, 0.30, 2020.00, 'USD'),
(3, 1, 'Transfer', 'Jane Smith', '250700222222', '2025-09-03 19:00:00', 20.00, 0.10, 2040.00, 'USD');

-- (repeat similar structured incomes for users 2–5 …)

-- =========================
-- SYSTEM LOGS (5 per user = 25 total)
-- =========================
-- INSERT INTO system_logs (status, transaction_id) VALUES
-- ('SUCCESS', 1),
-- ('FAILED', 2),
-- ('PENDING', 3),
-- ('SUCCESS', 4),
-- ('SUCCESS', 5),
-- ('SUCCESS', 6),
-- ('FAILED', 7),
-- ('SUCCESS', 8),
-- ('PENDING', 9),
-- ('SUCCESS', 10),
-- ('FAILED', 11),
-- ('SUCCESS', 12),
-- ('PENDING', 13),
-- ('SUCCESS', 14),
-- ('FAILED', 15),
-- ('SUCCESS', 16),
-- ('SUCCESS', 17),
-- ('FAILED', 18),
-- ('SUCCESS', 19),
-- ('PENDING', 20),
-- ('SUCCESS', 21),
-- ('FAILED', 22),
-- ('SUCCESS', 23),
-- ('PENDING', 24),
-- ('SUCCESS', 25);