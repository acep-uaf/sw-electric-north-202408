import geopandas as gpd

# user functions
from functions.api_geo import geo_save

# save community locations from DCCED
geo_save(
    geo_input = 'https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/dcced_communities.geojson')


# # Statewide Climate Threat Assessment (flood, erosion, permafrost)
# # Getting a 400 from the server, not sure what's up.
# geo_save(
#     geo_input = 'https://maps.commerce.alaska.gov/server/rest/services/Climate_Related/Statewide_Threat_Assessment_by_Community/MapServer/0/', 
#     geo_output = 'data/raw/dcced_climate_threat_assessment.geojson'
# )