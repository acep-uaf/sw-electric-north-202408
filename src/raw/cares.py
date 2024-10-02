import geopandas as gpd

# user functions
from functions.api_geo import geo_save


# save Electric North boundary (from .gitignored directory, downloaded from Google Drive) to file 
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_outline.shp',
    geo_output = 'data/raw/cares_boundary.geojson')

# save Electric North regional grids (from .gitignored directory, downloaded from Google Drive) to file
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_regionalGrids.shp',
    geo_output = 'data/raw/cares_regional_grids.geojson')

# save Electric North regional grid capacity (from .gitignored directory, downloaded from Google Drive) to file
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_regionalGrids_capacity.shp',
    geo_output = 'data/raw/cares_regional_grids_capacity.geojson')

geo_save(
    geo_input = 'data/source/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp',
    geo_output = 'data/raw/cares_transmission.geojson'
)


