import pandas as pd
import geopandas as gpd

df = pd.read_csv('data/source/gppdb/global_power_plant_database.csv')

gdf = gpd.GeoDataFrame(df, 
    geometry = gpd.points_from_xy(df['latitude'], df['longitude']), 
    crs = 'EPSG:4326')

gdf.to_file('data/raw/gppdb_powerplants.geojson', driver='GeoJSON')
