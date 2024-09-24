import geopandas as gpd

# user functions
from functions.api_geo import geo_save

# save community locations from DCCED
geo_save(
    geo_input = 'https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/dcced/data/dcced_communities.geojson')
