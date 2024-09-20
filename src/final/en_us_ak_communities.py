import geopandas as gpd

dcced_communities= gpd.read_file('data/raw/dcced_communities.geojson')

communities = dcced_communities[dcced_communities['CommunityTypeName'].isin([
    'Unincorporated',
    'Unincorporated CDP',
    '1st Class City',
    '2nd Class City',
    'Home Rule City',
    'CDP'
    ])]

communities = communities[['CommunityName', 'CommunityTypeName', 'x', 'y', 'geometry']]

communities.explore()
communities.to_file('data/derived/communities.geojson')


# left join to usgs gnis data by nearest neighbor
usgs_places = gpd.read_file('data/raw/usgs_places.geojson')
usgs_places.rename(columns={
    'gaz_id' : 'gnis',
    'gaz_name' : 'usgs_name'}, 
    inplace=True)

places = usgs_places[[
    'gnis', 
    'usgs_name', 
    'geometry'
]]

sjoin_distance = places.sjoin_nearest(communities, how='left', distance_col='distance', max_distance=1000)








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



merged = sales_report.merge(places, on='gnis')
merged = gpd.GeoDataFrame(merged, geometry='geometry', crs=usgs_places.crs)


# load polygon of regional grid boundaries
# remove communities inside of the grid boundaries



merged.explore()

merged.to_file('data/final/en_us_ak_communities.geojson')







# # places[places["CommunityTypeName].isin(list)]
# places[places['CommunityName'].isin(['Healy'])]





# want single sales reporting ids for multiple communities