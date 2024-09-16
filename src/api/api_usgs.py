import pandas as pd
import geopandas as gpd

# user functions
from src.functions.api_xlsx import xlsx_url_to_file
from src.functions.api_geo import geo_save


# save GNIS incorporated places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/1/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/gnis_incorporated.geojson'
)
incorporated = gpd.read_file('data/raw/gnis_incorporated.geojson')
incorporated.explore()


# save GNIS unincorporated places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/2/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/gnis_unincorporated.geojson'
)
unincorporated = gpd.read_file('data/raw/gnis_unincorporated.geojson')
unincorporated.explore()

# save GNIS places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/3/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/gnis_places.geojson'
)
places = gpd.read_file('data/raw/gnis_places.geojson')
places.explore()


tmp = places[places['gaz_name' == 'Aniak']]
