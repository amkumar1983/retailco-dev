CREATE TABLE [dbo].[dim_product] (

	[product_id] int NULL, 
	[product_name] varchar(100) NULL, 
	[category] varchar(50) NULL, 
	[unit_price] decimal(10,2) NULL, 
	[unit_cost] decimal(10,2) NULL
);