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


spark.sql("""
CREATE OR REPLACE TABLE gold_sales_by_day_region AS
SELECT s.order_date,
st.region, p.category,
SUM(s.net_amount) AS revenue,
SUM(s.quantity) AS units,
COUNT(*) AS orders
FROM silver_sales s
JOIN silver_dim_store st ON s.store_id = st.store_id
JOIN silver_dim_product p ON s.product_id = p.product_id
GROUP BY s.order_date, st.region, p.category
""")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("OPTIMIZE gold_sales_by_day_region")
spark.sql("OPTIMIZE silver_sales ZORDER BY (order_date)")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
