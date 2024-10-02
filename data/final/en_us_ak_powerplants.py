import geopandas as gpd
import pandas as pd

plants = gpd.read_file('data/derived/plants/plants.geojson')

plants.rename(inplace=True, columns={
    'plant_name': 'EN-plant_name',
    'primary_fuel': 'EN-primary_fuel',
    'other_fuel': 'EN-other_fuel',
    'capacity_mw': 'EN-installed_capacity'
})

out = plants

out.to_file('data/final/data/en_us_ak_powerplants.geojson', driver='GeoJSON')
