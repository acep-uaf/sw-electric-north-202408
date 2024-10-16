import geopandas as gpd

# user functions
from functions.api_geo import geo_save


geo_save(
    geo_input = 'data/source/fema_usa_structures/Deliverable20230728AK/AK_Structures.gdb',
    geo_output = 'data/raw/fema_building_footprints.geojson'
)
