# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "c2a006f7-10ab-4e0b-bf5a-7ddefef7e4c7",
# META       "default_lakehouse_name": "lh_retail",
# META       "default_lakehouse_workspace_id": "99de7f30-7a94-42a4-92fc-f1bc92d5d070",
# META       "known_lakehouses": [
# META         {
# META           "id": "c2a006f7-10ab-4e0b-bf5a-7ddefef7e4c7"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "faa3aced-cd10-b9b9-4780-552a702096a9",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import functions as F

raw = (spark.read.option("header", True).option("inferSchema", True)
.csv("Files/bronze/sales_raw_bronze.csv"))

#clean types,whitespaces, date formats, nulls

clean = (raw
    .withColumn("unit_price",F.trim(F.col("unit_price")).cast("double"))
    .withColumn("quantity", F.trim(F.col("quantity")).cast("int"))
    .withColumn("net_amount", F.trim(F.col("net_amount")).cast("double"))
    .withColumn("channel", F.initcap(F.trim(F.col("channel")))) # ONLINE -> Online
    # normalise the two date formats into one DATE column
    .withColumn("order_date",
    F.coalesce(
    F.to_date("order_date", "dd-MM-yyyy"),
    F.to_date("order_date", "yyyy-MM-dd")))
    .dropDuplicates(["order_id"]) # remove the injected dupes
    .filter(F.col("quantity").isNotNull()
    & F.col("net_amount").isNotNull()
    & F.col("customer_id").isNotNull()) # drop incomplete rows
    .withColumn("revenue_band",
    F.when(F.col("net_amount") < 500, "Low")
     .when(
         (F.col("net_amount") >= 500) &
         (F.col("net_amount") <= 2000),
         "Mid").otherwise("High"))
    .withColumn("run_date", F.to_date(F.lit(run_date), "yyyy-MM-dd"))     
    .withColumn("_loaded_at", F.current_timestamp())
    )

clean.write.mode("overwrite").option("overwriteschema",True).format("delta").saveAsTable("silver_sales")
#print("Silver rows:", spark.table("silver_sales").count())

row_count = spark.table("silver_sales").count()
mssparkutils.notebook.exit(str(row_count))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print("Silver rows:", spark.table("silver_sales").count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
