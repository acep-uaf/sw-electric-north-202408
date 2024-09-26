import geopandas as gpd
import pandas as pd

# load polygons with population data
# load points with intertie data
polys = gpd.read_file('data/raw/ak-dol.places2020/data/ak-dol.places2020.geojson')
points = gpd.read_file('data/raw/es/data/es_lookup_sales_report.geojson')
coords = gpd.read_file('data/raw/dcced/data/dcced_communities.geojson')


# clean:
#      rename colunmns
#      drop columns
#      drop duplicates?

polys.rename(inplace=True, columns={
    'NAME':'name',
    'STATE':'state',
    'PLACE':'place',
    'FIPS':'fips',
    'TOTALPOP':'total_population',
    'WHITE':'white',
    'BLACK':'black',
    'NATIVE':'native',
    'ASIAN':'asian',
    'PACISLAND':'pacific_islander',
    'OTHER':'other',
    'TWO_PLUS':'two_plus',
    'HISPANIC':'hispanic',
    'NATALNCOMB':'native_indian_combo',
    'GRPQTRS':'group_quarters',
    'HOUSEUNITS':'housing_units',
    'VACANT':'vacant_housing_units',
    'OCCUPIED':'occupied_housing_units'})


points.rename(inplace=True, columns={
    'Sales Reporting ID':'sales_reporting_id',
    'OPERATOR_AEA Operator ID':'aea_operator_id',
    'EIA operator Number':'eia_operator_number',
    'PCE Reporting ID':'pce_reporting_id',
    'EIA Sales reporting frequency':'eia_reporting_frequency',
    'PCE Sales reporting frequency':'pce_reporting_frequency',
    'Reporting Name':'reporting_name',
    'OPERATOR_Operator Name':'operator_name',
    'RCA CPCN':'rca_cpcn',
    'INTERTIE_Current Intertie ID':'intertie_id',
    'INTERTIE_Current Intertie name':'intertie_name',
    'Index Community':'community',
    'GNIS':'gnis',
    'Latitude':'latitude',
    'Longitude':'longitude',
    'AEA energy region':'aea_energy_region',
    'Communities reported':'communities_reported'
})

# drop duplicated sales reporting records
# investigate later
points.drop_duplicates(inplace=True, subset=['sales_reporting_id'], keep='last')

points = points[[
    'intertie_id', 
    'intertie_name', 
    'community', 
    'gnis', 
    'latitude', 
    'longitude',
    'communities_reported',
    'geometry']]





# Newhalen grid, index communitiy: Iliamna
newhalen_grid = pd.DataFrame({
    'fips': [
        '0253270',
        '0255030'
    ]
})
newhalen_grid['intertie_id'] = '123-1983'


# add railbelt community points
intertie_id == 215-1985

railbelt = pd.DataFrame({
    'community': [
        'Halibut Cove',
        'Seldovia',
        'Fox River',
        'Fritz Creek',
        'Diamond Ridge',
        'Anchor Point',
        'Nikolaevsk',
        'Happy Valley',
        'Ninilchick',
        'Clam Gulch',
        'Cohoe',
        'Kasilof',
        'Kalifornsky',
        'Soldotna',
        'Funny River',
        'Sterling',
        'Ridgeway',
        'Kenai',
        'Salamatof',
        'Nikiski',
        'Point Possession',
        'Cooper Landing',
        'Moose Pass',
        'Crown Point',
        'Primrose',
        'Bear Creek',
        'Lowell Point',
        'Whittier',
        'Tyonek',
        'Beluga',
        'Point McKenzie',
        'Susitna',
        'Knik River',
        'Butte',
        'Lazy Mountain',
        'Sutton-Alpine',
        'Buffalo Soapstone',
        'Fishhook',
        'Farm Loop',
        'Palmer',
        'Gateway',
        'South Lakes',
        'North Lakes',
        'Tanaina',
        'Knik-Fairview',
        'Meadow Lakes',
        'Houston',
        'Big Lake',
        'Willow',
        'Susitna North',
        'Talkeetna',
        'Chase',
        'Cantwell',
        'Denali Park',
        'Healy',
        'Ferry',
        'Anderson',
        'Nenana',
        'Four Mile Road',
        'Chena Ridge',
        'Ester',
        'Goldstream',
        'College',
        'Farmers Loop',
        'Fox',
        'Steele Creek',
        'Two Rivers',
        'Pleasant Valley',
        'Badger',
        'North Pole',
        'Moose Creek',
        'Salcha',
        'Harding-Birch Lakes',
        'Big Delta',
        'Delta Junction',
        'Fort Greely',
        'Deltana']})

railbelt['intertie_id'] = '215-1985'



















# left-join points with polygons
left_join = points.sjoin_nearest(polys, how='left', max_distance=1000)
right_join = points.sjoin_nearest(polys, how='right', distance_col = 'distance')
no_match = right_join[right_join['distance'] > 1000]

m = polys.explore()
no_match.explore(
    m=m,
    color='red'
)





##########
TODO
# add railbelt communities (find/make list of communities with point data, )
test = gpd.read_file('data/derived/regional_grids/regional_grids.geojson')
test.explore()





# start with places polygons
places = gpd.read_file('data/raw/ak-dol.places2020/data/ak-dol.places2020.geojson')

m = places.explore(
    color='blue'
)
m

# test.explore(
#     m=m,
#     color='green'
# )

# add transmission lines
lines = gpd.read_file('data/derived/transmission/transmission.geojson')

lines.explore(
    m=m,
    color='black'
)

# # add more data
# plants = gpd.read_file('data/derived/plants/plants.geojson')

# plants.explore(
#     m=m,
#     color = 'orange'
# )

no_match.explore(
    m=m,
    color = 'red'
)
