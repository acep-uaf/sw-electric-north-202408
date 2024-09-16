import pandas as pd
import geopandas as gpd


from src.pipeline.api_xlsx import xlsx_url_to_file
from src.pipeline.api_geo import geo_save


layer_url = "https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/1"
params = {
    'outFields': '*',
    'where': 'state_alpha%3D%27AK%27',
    'f': 'geojson'
}

# Construct the URL with query parameters
url = layer_url + '/query?' + '&'.join([f'{key}={value}' for key, value in params.items()])
print(url)

geo_save(
    geo_input = url,
    geo_output = 'data/derived/so_much_testing.geojson'
)

test = gpd.read_file('data/derived/so_much_testing.geojson')


test.plot()


test['OBJECTID'].nunique()

tmp = test[['OBJECTID', 'geometry']]
tmp.plot()
