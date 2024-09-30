# this script is for adding plant_id to AETR generation data

import geopandas as gpd
import pandas as pd

plants = gpd.read_file('data/derived/plants/plants.geojson')
aetr = gpd.read_file('data/raw/aetr/data/aetr_generation.csv')

a = aetr[['plant_name']].drop_duplicates()

p = plants[['plant_name', 'aea_plant_id']]


merged = pd.merge(a, p, on='plant_name', how='left')
m = merged.dropna()

# make dictionary of matching
merged_dict = dict(zip(m['plant_name'], m['aea_plant_id']))


# make a dictionary of plant names and intertie_ids
manual_dict = {
    'Alaska Environmental': 'P14', # Delta Wind Farm
    'Allakaket, Alatna': 'P30',
    'Aurora Energy': 'P109',
    'Aurora Energy LLC Chena': 'P109',
    # 'Banner Peak Wind Farm': , # Nome Grid, decommissioned in 2011?
    'Bettles, Evansville': 'P31', 
    'Blue Lake': 'P240', # Sitka Grid
    'Chignik': 'P116', 
    'Craig (AK)': 'P20', 
    'Dillingham, Aleknagik': 'P224',
    'Eagle, Eagle Village': 'P34', 
    'Eklutna Lake': 'P102', 
    'Falls Creek': 'P35', # Gustavus, is this the hydro plant?
    'Fort Yukon': 'P154', 
    'Galena': 'P144',
    'Goat Lake': 'P16', # Upper Lynn Canal Grid
    # 'Hank Nikkels Plant 1': railbelt, # decommissioned in 2016?
    'Iliamna, Newhalen, Nondalton': 'P162',
    'Kalskag': 'P77',
    'Kasidaya Creek': 'P17', # Upper Lynn Canal Grid
    'Kodiak': 'P182', 
    'Kotzebue Hybrid': 'P189',
    'Lake Dorothy': 'P10',
    'NSB Atqasuk Utility': 'P217', # Atqasuk Grid
    'NSB Kaktovik Utility': 'P218', # Kaktovik Grid
    'NSB Nuiqsut Utility': 'P219', # Nuiqsut Grid
    'NSB Point Hope Utility': 'P220', # Point Hope Grid
    'Naknek, South Naknek, King Salmon': 'P207',
    'Nikiski Combined Cycle': 'P157', 
    'Northway, Northway Village, Northway Junction': 'P25',
    'Nymans Plant': 'P183', # Kodiak
    'Petersburg': 'P229', # Petersburg
    'Pillar Mountain': 'P184', # Kodiak
    'Port Lions': 'P185', # Kodiak
    "Saint Mary's, Andreafsky": 'P67',
    'Seward (AK)': 'P67', 
    'Sheldon Point': 'P223', # Nunam Iqua
    'Slana': 'P27',
    'TDX CT1/CT2': 'P254', # Deadhorse Grid
    'Tazimina': 'P162', # Newhalen Grid
    'Terror Lake': 'P187', # Kodiak
    'Tok, Tanacross': 'P29'
}

# combine dictionaries
lookup_dict = {**merged_dict, **manual_dict}

# map the combined dictionary back onto the initially joined data
merged['aea_plant_id'] = merged['plant_name'].map(lookup_dict)

lookup = merged

lookup.to_csv('data/derived/lookup_plant_name_id/lookup_plant_name_id.csv', index=False)

load = pd.read_csv('data/derived/lookup_plant_name_id/lookup_plant_name_id.csv')
