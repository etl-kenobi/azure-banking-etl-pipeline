
# 📘 Process Flow Documentation

This document outlines the key stages in the Azure Banking ETL Pipeline project:

1. **Source**: On-premise banking data (CSV format)
2. **Ingestion**: Loaded into ADLS Gen2 via ADF Copy Activity → Bronze layer
3. **Transformation**:
   - Synapse Notebooks clean & enrich data → Silver layer
   - Aggregation & Joins applied → Gold layer
4. **Serving**: SQL Serverless provides external views for analytics teams
5. **CI/CD**: Pipelines managed via Git integration with ARM templates

Monitoring, alerts, and retry policies configured in ADF.
