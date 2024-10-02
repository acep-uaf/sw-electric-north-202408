import geopandas as gpd

# user functions
from functions.api_geo import geo_save

geo_save(
    geo_input = 'https://live.laborstats.alaska.gov/cen/maps/gis/Places2020.zip',
    geo_output = 'data/raw/dol_places_2020.geojson'
)
