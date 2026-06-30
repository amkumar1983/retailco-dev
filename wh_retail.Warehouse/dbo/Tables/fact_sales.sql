CREATE TABLE [dbo].[fact_sales] (

	[order_id] bigint NULL, 
	[date_key] int NULL, 
	[customer_id] int NULL, 
	[product_id] int NULL, 
	[store_id] int NULL, 
	[quantity] int NULL, 
	[unit_price] decimal(10,2) NULL, 
	[discount_pct] int NULL, 
	[net_amount] decimal(12,2) NULL, 
	[channel] varchar(20) NULL
);