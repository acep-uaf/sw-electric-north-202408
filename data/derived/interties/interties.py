import geopandas as gpd
import pandas as pd

# read
lookup_interties = pd.read_csv('data/raw/es/data/es_lookup_interties.csv')

# rename columns
lookup_interties.rename(inplace=True, columns={
    'Intertie Unique ID Name': 'intertie_name',
    'Current ID': 'current',
    'Communities Intertied': 'communities_intertied',
    'Month of intertie': 'month_of_intertie',
    'Year of intertie': 'year_of_intertie',
    'AEA energy region': 'aea_energy_region',
    'Source': 'source'
})

# intertie name cleaning
lookup_interties['intertie_name'] = lookup_interties['intertie_name'].str.replace('_grid', ' Grid', regex=True)

# pull columns
interties = lookup_interties[[
    'intertie_id',
    'intertie_name',
    'current',
    'aea_energy_region',
    'source'
]]

# select only current interties (current == True)
interties = interties[interties['current'] == True]

# write
interties.to_csv('data/derived/interties/interties.csv', index=False)
