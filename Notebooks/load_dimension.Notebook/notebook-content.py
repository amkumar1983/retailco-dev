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

#load the three dimensions (clean already) as Delta:
DimName="customer"
spark.read.option("header",True).option("inferSchema",True).csv(f"Files/bronze/dim_{DimName}.csv").write.mode("overwrite").format("delta").saveAsTable(f"silver_dim_{DimName}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
