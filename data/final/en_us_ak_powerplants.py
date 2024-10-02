import geopandas as gpd
import pandas as pd

plants = gpd.read_file('data/derived/plants/plants.geojson')

test = plants[[
    'aea_plant_id',
    'plant_name',
    'intertie_id',
    'capacity_mw',
    'latitude',
    'longitude',
    
]]