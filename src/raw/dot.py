import geopandas as gpd

from functions.api_geo import geo_save

geo_save(
    geo_input = 'https://services.arcgis.com/r4A0V7UzH9fcLVvv/arcgis/rest/services/Roads_AKDOT/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/dot_roads.geojson'
)

geo_save(
    geo_input = 'https://services.arcgis.com/r4A0V7UzH9fcLVvv/arcgis/rest/services/Routes/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/dot_routes.geojson'
)