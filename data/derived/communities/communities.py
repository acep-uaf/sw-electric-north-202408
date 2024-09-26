import geopandas as gpd
import pandas as pd

# load polygons with population data
# load points with intertie data
polys = gpd.read_file('data/raw/ak-dol.places2020/data/ak-dol.places2020.geojson')
lookup = gpd.read_file('data/derived/lookup_fips_interties/data/lookup_fips_interties.csv')

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

# drop 'CDP', 'city', 'municipality', 'city and borough'
polys['name'] = polys['name'].str.replace(r'\b(CDP|city|and|borough|municipality)\b', '', regex=True).str.strip()



# have polygons with fips
# join lookup_interties_fips to get intertie_id on polygons
polys_interties = pd.merge(polys, lookup, how='left', on='fips')


# pull aggregated intertie data (capacity, generation)

