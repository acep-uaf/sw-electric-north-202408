import geopandas as gpd
import pandas as pd

generation = pd.read_csv('data/derived/generation/generation.csv')
plants = gpd.read_file('data/derived/plants/plants.geojson')


# pull generation data, join to plants
plants_monthly_generation = pd.merge(generation, plants, how='left', on='aea_plant_id')

# average by year
plants_annual_generation = plants_monthly_generation.groupby([
    'aea_plant_id', 
    'intertie_id',
    'year',
    'fuel_type'
    ])['generation'].mean().reset_index()

# pull year
plants_annual_average = plants_annual_generation[plants_annual_generation['year'] == 2018]

# sum by intertie and fuel source
intertie_annual_source = plants_annual_average.groupby(['intertie_id', 'year', 'fuel_type'])['generation'].sum().reset_index()
# sum all sources generation by intertie
intertie_annual = plants_annual_average.groupby(['intertie_id','year'])['generation'].sum().reset_index()

# define the list of renewable sources
renewable_sources = ['Hydro', 'Solar', 'Wind']

# sum renewable generation by intertie
renewable_generation = intertie_annual_source.loc[
    (intertie_annual_source['fuel_type'].isin(renewable_sources)), 
    ['intertie_id', 'generation']
].groupby('intertie_id')['generation'].sum().reset_index()

# sum all sources generation by intertie
intertie_annual = intertie_annual_source.groupby('intertie_id')['generation'].sum().reset_index()

# calculate ratio of renewable to non-renewable
renewable_ratio = pd.merge(intertie_annual, renewable_generation, how='left', on='intertie_id').fillna(0)
renewable_ratio['renewable_ratio'] = renewable_ratio['generation_y']/renewable_ratio['generation_x']
renewable_ratio = renewable_ratio[['intertie_id', 'renewable_ratio']]

out = pd.merge(intertie_annual, renewable_ratio, how='left', on='intertie_id')

out.to_csv('data/final/data/renewable_generation.csv', index=False)

