from pyspark.sql.functions import col, when

df = spark.read.csv("abfss://bronze@datalake/transactions.csv", header=True, inferSchema=True)

df_enriched = df.withColumn("high_value_flag", when(col("txn_amount") > 500, "Y").otherwise("N"))

df_enriched.write.format("delta").mode("overwrite").save("abfss://silver@datalake/transactions_enriched")