DELETE FROM customers WHERE customer_id IN (1);
DELETE FROM transaction_category WHERE customer_id IN (1);
DELETE FROM savings_account WHERE customer_id IN (1);
DELETE FROM sms WHERE customer_id IN (1);   