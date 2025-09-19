CREATE DATABASE expense_tracker;
USE expense_tracker;

CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  phone_number VARCHAR(20),
  email VARCHAR(150),
  password_hash VARCHAR(500),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id),
  KEY idx_customer (last_name, phone_number, email, created_at)
);

CREATE TABLE transaction_category (
  category_id INT AUTO_INCREMENT,
  customer_id INT,
  transaction_type VARCHAR(50),
  PRIMARY KEY (category_id),
  KEY idx_category (transaction_type),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE savings_account (
  account_id INT AUTO_INCREMENT,
  customer_id INT,
  balance DECIMAL(15,2) DEFAULT 0.00,
  currency VARCHAR(10),
  description VARCHAR(255),
  PRIMARY KEY (account_id),
  KEY idx_savings (balance, currency),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE sms (
  sms_id INT AUTO_INCREMENT,
  customer_id INT,
  address VARCHAR(255),
  date_sent DATETIME,
  type VARCHAR(50),
  service_center VARCHAR(255),
  body TEXT,
  PRIMARY KEY (sms_id),
  KEY idx_sms (address, date_sent, type, service_center),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE expense (
  transaction_id INT AUTO_INCREMENT,
  sms_id INT,
  customer_id INT,
  transaction_type VARCHAR(50),
  beneficiary_name VARCHAR(150),
  beneficiary_phone_number VARCHAR(20),
  transaction_date DATETIME,
  amount DECIMAL(15,2),
  fee_paid DECIMAL(15,2),
  balance_after DECIMAL(15,2),
  currency VARCHAR(10),
  PRIMARY KEY (transaction_id),
  KEY idx_expense (transaction_type, beneficiary_name, transaction_date, amount, fee_paid, balance_after, currency),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (sms_id) REFERENCES sms (sms_id)
);

CREATE TABLE income (
  transaction_id INT AUTO_INCREMENT,
  sms_id INT,
  customer_id INT,
  transaction_type VARCHAR(50),
  sender_name VARCHAR(150),
  sender_phone_number VARCHAR(20),
  transaction_date DATETIME,
  amount DECIMAL(15,2),
  fee_paid DECIMAL(15,2),
  balance_after DECIMAL(15,2),
  currency VARCHAR(10),
  PRIMARY KEY (transaction_id),
  KEY idx_income (transaction_type, sender_name, transaction_date, amount, fee_paid, balance_after, currency),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (sms_id) REFERENCES sms (sms_id)
);

CREATE TABLE system_logs (
  log_id INT AUTO_INCREMENT,
  status VARCHAR(50),
  transaction_id INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (log_id),
  KEY idx_logs (status, created_at),
  FOREIGN KEY (transaction_id) REFERENCES expense (transaction_id)
);