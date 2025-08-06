# Azure Banking ETL Pipeline 🚀

This project simulates a real-world banking data pipeline using Azure cloud services and open-source tools. It demonstrates an end-to-end ETL (Extract, Transform, Load) process for ingesting, transforming, and analyzing banking datasets using:

- **Azure Data Factory** for orchestrating data pipelines
- **Azure Data Lake Storage** for raw/staged/processed layers
- **Azure Databricks / PySpark** for transformations
- **Azure Synapse SQL Serverless** for querying data lake with SQL
- **Delta Lake format** for scalable and ACID-compliant storage

---

## 📁 Folder Structure

```
azure-banking-etl-pipeline/
├── adf-pipeline/            # ADF JSON definition
├── architecture/            # Diagrams and design artifacts
├── datasets/                # Sample input CSVs
├── notebooks/               # PySpark scripts (Databricks-ready)
├── synapse-sql/             # SQL views for Synapse Serverless
├── docs/                    # Walkthroughs and use cases
└── README.md                # You’re here!
```

---

## 🏦 Use Case

A fictional bank needs to modernize its legacy data pipeline. This solution:
- Migrates customer and transaction data to Azure
- Cleans & enriches records using PySpark
- Stores output in Delta format
- Enables analytics using Synapse SQL views

---

## 🛠️ Tools Used

- Azure Data Factory
- Azure Data Lake Gen2
- Azure Synapse Analytics (SQL Serverless)
- Azure Databricks
- PySpark
- Delta Lake

---

## 📊 Sample Outputs

- Identify high-value customers
- Aggregate spend by region
- Join transactions with customer metadata

---

## 🧠 Learning Outcomes

- Hands-on orchestration with ADF
- Modular PySpark scripts for batch ETL
- SQL-based reporting on Delta tables
