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
# META     "warehouse": {
# META       "known_warehouses": []
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.functions import (
    col,
    date_format,
    year,
    quarter,
    month,
    dayofmonth,
    weekofyear,
    when,
    dayofweek,
    lit
)

# Generate dates from 2020-01-01 to 2035-12-31
df = spark.sql("""
SELECT explode(
    sequence(
        to_date('2020-01-01'),
        to_date('2035-12-31'),
        interval 1 day
    )
) AS full_date
""")

# Create Date Dimension
dim_date = (
    df
    .withColumn("date_key", date_format(col("full_date"), "yyyyMMdd").cast("int"))
    .withColumn("year", year(col("full_date")))
    .withColumn("quarter", quarter(col("full_date")))
    .withColumn("month", month(col("full_date")))
    .withColumn("month_name", date_format(col("full_date"), "MMMM"))
    .withColumn("day", dayofmonth(col("full_date")))
    .withColumn("day_name", date_format(col("full_date"), "EEEE"))
    .withColumn("week_of_year", weekofyear(col("full_date")))
    .withColumn(
        "is_weekend",
        when(dayofweek(col("full_date")).isin(1, 7), lit(True))
        .otherwise(lit(False))
    )
)

# Display sample
display(dim_date)

# Save to Warehouse table
(
    dim_date.write
    .mode("overwrite")
    .saveAsTable("dim_date")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
