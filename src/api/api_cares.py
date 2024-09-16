import geopandas as gpd

# user functions
from src.api.functions.api_geo import geo_save


# save Electric North boundary (from .gitignored directory, downloaded from Google Drive) to file 
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_outline.shp',
    geo_output = 'data/raw/en_boundary.geojson')

# save Electric North regional grids (from .gitignored directory, downloaded from Google Drive) to file
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_regionalGrids.shp',
    geo_output = 'data/raw/en_regional_grids.geojson')

# save Electric North regional grid capacity (from .gitignored directory, downloaded from Google Drive) to file
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_regionalGrids_capacity.shp',
    geo_output = 'data/raw/en_regional_grids_capacity.geojson')


# clean up string voltage, convert to numeric, cut to 100 KV
def voltage_cleaning(input, output):
    raw = gpd.read_file(input)
    raw.Voltage = (raw.Voltage.str.replace(r'[<KV-]', '', regex=True)
                        .str.split('-').str[0]
                        .astype(float).round())
    clean = raw[raw['Voltage'] >= 35]
    clean.to_file(output)

voltage_cleaning(
    input = 'data/source/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp',
    output = 'data/derived/transmission.geojson')

# test = gpd.read_file('data/raw/en_boundary.geojson')
# test.explore()
