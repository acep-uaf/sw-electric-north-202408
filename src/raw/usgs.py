import geopandas as gpd

# user functions
from functions.api_geo import geo_save


# save GNIS incorporated places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/1/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/usgs_incorporated.geojson'
)


# save GNIS unincorporated places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/2/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/usgs_unincorporated.geojson'
)

# save GNIS places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/3/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/usgs_places.geojson'
)

# US Wind Turbine Database
geo_save(
    geo_input = 'data/source/uswtdb/uswtdb_v7_1_20240814.geojson',
    geo_output = 'data/raw/usgs_uswtdb.geojson',
    crs=4326
)

# National Boundary Dataset
# It's there in /sources, but seems to be repackaged Census data
# I'm not sure the value of this data, preserving code for posterity

