# Project Walkthrough 🧭

This document walks you through how the Azure Banking ETL Pipeline works end to end.

---

## Step 1: Data Ingestion (ADF)

- Two datasets: `customers.csv` and `transactions.csv`
- ADF pipeline ingests these CSVs from blob storage to ADLS
- Data lands in the **Bronze** layer (raw zone)

---

## Step 2: Data Cleaning & Transformation (PySpark in Databricks)

- `clean_customers.py`: Standardizes name fields, deduplicates records
- `transform_transactions.py`: Adds flags like `is_high_value`
- `join_customer_txns.py`: Combines both datasets into **Silver** zone

---

## Step 3: Analytical Views (Synapse Serverless)

- `create_external_tables.sql`: Creates SQL views over Delta folders
- `gold_view_aggregations.sql`: Prepares aggregation metrics (e.g., total spend by customer)

---

## Step 4: Output

- Query `gold` views using Synapse Studio
- Perform ad-hoc analysis or visualize in Power BI (future scope)
