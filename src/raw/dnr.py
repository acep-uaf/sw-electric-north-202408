import geopandas as gpd

# user functions
from functions.api_geo import geo_save

# save ak_coastline to file from DNR
geo_save(
    geo_input = 'https://arcgis.dnr.alaska.gov/arcgis/rest/services/OpenData/Physical_AlaskaCoast/MapServer/1/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/dnr_coastline.geojson')
