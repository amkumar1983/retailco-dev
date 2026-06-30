[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "lh_retail_DataDestination", IsNewTarget = false], Settings = [Kind = "Manual", AllowCreation = false, ColumnSettings = [Mappings = {[SourceColumnName = "customer_id", DestinationColumnName = "customer_id"], [SourceColumnName = "customer_name", DestinationColumnName = "customer_name"], [SourceColumnName = "email", DestinationColumnName = "email"], [SourceColumnName = "loyalty_tier", DestinationColumnName = "loyalty_tier"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared lh_retail = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "99de7f30-7a94-42a4-92fc-f1bc92d5d070"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "c2a006f7-10ab-4e0b-bf5a-7ddefef7e4c7"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "silver_dim_customer", ItemKind = "Table"]}[Data],
  TransformTable = Table.TransformColumns(#"Navigation 2", {{"loyalty_tier", Text.Upper}}),
  #"Choose columns" = Table.SelectColumns(TransformTable, {"customer_id", "customer_name", "email", "loyalty_tier"})
in
 #"Choose columns";
shared lh_retail_DataDestination = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "."]}[Data],
  Navigation_2 = Navigation_1{[displayName = "wh_retail"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "dbo"]}[Data],
  TableNavigation = Navigation_3{[Name = "dim_customer"]}[Data]
in
  TableNavigation;
