import pandas as pd
import geopandas as gpd

gaz = pd.read_csv('https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_gaz_place_02.txt', delimiter="\t")


gaz.rename(inplace=True, columns={
    'USPS': 'usps',
    'GEOID': 'geoid',
    'ANSICODE': 'ansi_code',
    'NAME': 'name',
    'LSAD': 'lsad',
    'FUNCSTAT': 'funcstat',
    'ALAND': 'area_land',
    'AWATER': 'area_water',
    'ALAND_SQMI': 'area_land_sq_mi',
    'AWATER_SQMI': 'area_water_sq_mi',
    'INTPTLAT': 'latitude',
    'INTPTLONG                                                                                                 ': 'longitude' # what is this? spaces needed for string recognition??
})





# convert to geodataframe
gdf = gpd.GeoDataFrame(
    gaz, geometry=gpd.points_from_xy(gaz.longitude, gaz.latitude), crs='EPSG:4326'
)

gdf.explore()
# problems: sitka, juneau
    
gdf.to_file('data/raw/census_2024_gaz_places.geojson', driver='GeoJSON')

