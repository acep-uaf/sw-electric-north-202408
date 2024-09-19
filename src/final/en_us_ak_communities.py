import geopandas as gpd

derived_sales_report = gpd.read_file('data/derived/lookup_sales_report.geojson')

derived_sales_report.rename(columns={
    'Sales Reporting ID' : 'sr_id',
    'OPERATOR_AEA Operator ID' : 'aea_operator_id',
    'EIA operator Number' : 'eia_operator_id',
    'PCE Reporting ID' : 'pce_id',
    'Reporting Name' : 'reporting_name',
    'OPERATOR_Operator Name' : 'operator_name',
    'RCA CPCN' : 'rca_cpcn', 
    'INTERTIE_Current Intertie ID' : 'intertie_id',
    'INTERTIE_Current Intertie name' : 'name', 
    'Index Community' : 'index_community', 
    'GNIS' : 'gnis', 
    'Latitude' : 'latitude', 
    'Longitude' : 'longitude'}, 
    inplace=True)

sales_report = derived_sales_report[[
    'sr_id',
    'aea_operator_id',
    'eia_operator_id',
    'pce_id',
    'rca_cpcn', 
    'intertie_id',
    'gnis'
]]

usgs_places = gpd.read_file('data/raw/usgs_places.geojson')
usgs_places.rename(columns={
    'gaz_id' : 'gnis',
    'gaz_name' : 'name'}, 
    inplace=True)

places = usgs_places[[
    'gnis', 
    'name', 
    'geometry'
]]

merged = sales_report.merge(places, on='gnis')
merged = gpd.GeoDataFrame(merged, geometry='geometry', crs=usgs_places.crs)

merged.explore()
