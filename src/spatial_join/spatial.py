import geopandas as gpd
import pandas as pd

aetr = gpd.read_file('data/raw/aetr_generation.csv')
a = aetr[['plant_name']].drop_duplicates()

lookup = gpd.read_file('data/derived/lookup_plants.geojson')
l = lookup[['plant_name']].drop_duplicates()


test = a.merge(l, on='plant_name', how='outer', indicator=True)


# pull generation by fuel type data (source?), 
gen = pd.read_csv('data/derived/gen_fuel_type.csv')

# join to plant lookup, dropping plant lookup names (bad strings)
raw_lookup = gpd.read_file('data/derived/lookup_plants.geojson')
lookup = raw_lookup.loc[:, ~raw_lookup.columns.isin(['plant_name'])]

# extract names and lat/longs
merged = gen.merge(lookup, left_on='PLANTS_AEA plant ID', right_on='AEA Plant ID')

out = merged[['PLANTS_AEA plant ID', 'PLANTS_Plant Name', 'Latitude', 'longitude', 'geometry']].drop_duplicates()

aetr = gpd.read_file('data/raw/aetr_generation.csv')
a = aetr[['plant_name']].drop_duplicates()
test = a.merge(out, left_on='plant_name', right_on='PLANTS_AEA plant ID', how='outer', indicator=True)
