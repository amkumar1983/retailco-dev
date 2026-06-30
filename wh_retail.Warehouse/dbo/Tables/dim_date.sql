CREATE TABLE [dbo].[dim_date] (

	[date_key] int NOT NULL, 
	[full_date] date NOT NULL, 
	[year] int NOT NULL, 
	[quarter] int NOT NULL, 
	[month] int NOT NULL, 
	[month_name] varchar(15) NOT NULL, 
	[day] int NOT NULL, 
	[day_name] varchar(10) NOT NULL, 
	[week_of_year] int NOT NULL, 
	[is_weekend] bit NOT NULL
);


GO
ALTER TABLE [dbo].[dim_date] ADD CONSTRAINT pk_dim_date primary key NONCLUSTERED ([date_key]);