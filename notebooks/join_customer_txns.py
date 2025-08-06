df_cust = spark.read.format("delta").load("abfss://silver@datalake/customers_cleaned")
df_txns = spark.read.format("delta").load("abfss://silver@datalake/transactions_enriched")

df_joined = df_txns.join(df_cust, on="customer_id", how="inner")

df_joined.write.format("delta").mode("overwrite").save("abfss://gold@datalake/customer_transaction_gold")