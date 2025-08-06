SELECT 
    country,
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(txn_id) AS total_transactions,
    SUM(txn_amount) AS total_txn_amount
FROM OPENROWSET(
    BULK 'gold/customer_transaction_gold/',
    DATA_SOURCE = 'your_external_data_source',
    FORMAT = 'DELTA'
) AS gold_data
GROUP BY country;