from pyspark.sql.functions import col, lower, trim

df = spark.read.csv("abfss://bronze@datalake/customers.csv", header=True, inferSchema=True)

df_cleaned = df.withColumn("email", lower(trim(col("email")))) \
               .withColumn("first_name", trim(col("first_name"))) \
               .withColumn("last_name", trim(col("last_name")))

df_cleaned.write.format("delta").mode("overwrite").save("abfss://silver@datalake/customers_cleaned")