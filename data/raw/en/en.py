import geopandas as gpd

# user functions
from functions.api_geo import geo_save


# first and foremost, this geodatabase represents our target output
# save geodatabase to file as geojson
geo_save(
    geo_input = 'data/source/Alaska_population_locations.gdb.zip',
    geo_output = 'data/raw/en/data/en_population_locations.geojson')

# # read to memory for testing
# target = gpd.read_file('data/raw/alaska_population_locations.geojson')

