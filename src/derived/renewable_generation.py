import geopandas as gpd
import pandas as pd

generation = pd.read_csv('data/derived/generation.csv')
plants = gpd.read_file('data/derived/plants.geojson')

year = 2018

# rename column generation
generation.rename(inplace=True, columns={'generation': 'generation_mwh'})

# pull generation data, join to plants
plants_monthly = pd.merge(generation, plants, how='left', on='aea_plant_id')

# average by year
plants_annual = plants_monthly.groupby([
    'aea_plant_id', 
    'intertie_id',
    'year',
    'fuel_type'
    ])['generation_mwh'].mean().reset_index()

# sum all sources generation by intertie
sum_generation = plants_annual.groupby(['intertie_id', 'year'])['generation_mwh'].sum().reset_index()

# define the list of renewable sources
renewable_sources = ['Hydro', 'Solar', 'Wind']
# sum renewable generation by intertie
sum_renewables = plants_annual.loc[
    (plants_annual['fuel_type'].isin(renewable_sources)), 
    ['intertie_id', 'year', 'generation_mwh']
].groupby(['intertie_id', 'year'])['generation_mwh'].sum().reset_index(
).rename(columns={'generation_mwh': 'renewable_generation_mwh'})

# merge total capacity with renewable capacity, set na's equal to 0 (inerties without renewables)
renewable_ratio = pd.merge(sum_generation, sum_renewables, how='left', on=['intertie_id', 'year']).fillna(0)

# calculate ratio of renewable to non-renewable
renewable_ratio['ratio_renewable_generation'] = renewable_ratio['renewable_generation_mwh']/renewable_ratio['generation_mwh']

out = renewable_ratio

out.to_csv('data/derived/renewable_generation.csv', index=False)

