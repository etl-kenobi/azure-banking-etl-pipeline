
# 🏦 Azure Banking ETL Pipeline

This project demonstrates an end-to-end data migration solution for a hypothetical banking dataset using Azure Data Factory, Azure Synapse Analytics, Delta Lake, and PySpark notebooks.

## 🚀 Use Case

Migrating on-premise customer and transaction data into an Azure-based Data Lakehouse using a medallion architecture (Bronze → Silver → Gold).

## 🛠 Tech Stack

- Azure Data Factory
- Azure Synapse Analytics
- Azure Data Lake Storage Gen2
- PySpark on Synapse Notebooks
- Delta Lake
- SQL Serverless

## 📁 Structure

```
azure-banking-etl-pipeline/
├── datasets/
├── notebooks/
├── adf-pipeline/
├── synapse-sql/
├── architecture/
└── docs/
```

## 📌 Features

- Ingestion from CSV to Bronze layer
- Data cleansing and enrichment in Silver
- Aggregated insights in Gold
- ADF pipeline orchestration
- Modular PySpark transformations
- SQL Serverless views for reporting

## 👨‍💻 Author

**Rahul Gurjar**  
GitHub: [etl-kenobi](https://github.com/etl-kenobi)
