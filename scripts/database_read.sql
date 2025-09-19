SELECT customr_id, first_name, last_name, phone_number, email FROM customers;
SELECT category_id, customer_id, transaction_type FROM transaction_category;
SELECT account_id, customer_id, balance, currency, description FROM savings_account;
SELECT sms_id, customer_id, address, date_sent, type, service_center, body FROM sms;
SELECT transaction_id, sms_id, customer_id, transaction_type, beneficiary_name, beneficiary_phone_number, transaction_date, amount, fee_paid, balance_after, currency FROM expense;
SELECT transaction_id, sms_id, customer_id, transaction_type, payer_name, payer_phone_number, transaction_date, amount, fee_received, balance_after, currency FROM income;