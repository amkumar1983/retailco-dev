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

# Welcome to your new notebook
# Type here in the cell editor to add code!

spark.sql("""
CREATE OR REPLACE TABLE gold_top_customers AS
SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    s.lifetime_revenue,
    s.total_orders
FROM (
    SELECT
        customer_id,
        SUM(net_amount) AS lifetime_revenue,
        COUNT(order_id) AS total_orders
    FROM silver_sales
    GROUP BY customer_id
) s
INNER JOIN silver_dim_customer c
    ON s.customer_id = c.customer_id
ORDER BY s.lifetime_revenue DESC
LIMIT 20
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM lh_retail.dbo.gold_top_customers LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
