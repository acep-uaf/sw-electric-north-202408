import pandas as pd
import geopandas as gpd


from src.pipeline.api_xlsx import xlsx_url_to_file
from src.pipeline.api_geo import geo_save

# first and foremost, this geodatabase represents our target output
# save geodatabase to file as geojson
geo_save(
    geo_input = 'data/source/Alaska_population_locations.gdb.zip',
    geo_output = 'data/raw/alaska_population_locations.geojson')
target = gpd.read_file('data/raw/alaska_population_locations.geojson')

tmp = target[target.duplicated(['Name_of_Settlement'], keep = False)]





# download infrastructure xlsx from Energy Stats Github repo, save to file
# pull plant locations, save as geojson
xlsx_url_to_file(
    xlsx_url = 'https://raw.githubusercontent.com/acep-uaf/ak-energy-statistics-2011_2021/main/workbooks/Energy_Stats_Infrastructure_2021.xlsx', 
    file = 'data/raw/Energy_Stats_Infrastructure_2021.xlsx')

df = pd.read_excel(
        'data/raw/Energy_Stats_Infrastructure_2021.xlsx',
        sheet_name = 'LOOKUP PLANTS 2023-11-13')

gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.Latitude), crs='EPSG:4326').to_crs(3338).to_file(
    'data/derived/plant_locations.geojson', driver='GeoJSON')



# download generation xlsx from Energy Stats Github repo, save to file
# pull data, save as geojson
xlsx_url_to_file(
    xlsx_url = 'https://github.com/acep-uaf/ak-energy-statistics-2011_2021/raw/main/workbooks/Energy_Stats_Generation_Tables.xlsx', 
    file = 'data/raw/Energy_Stats_Generation_Tables.xlsx')

df = pd.read_excel(
        'data/raw/Energy_Stats_Generation_Tables.xlsx',
        sheet_name = 'LOOKUP SalesReport 2023-11-13')

gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs='EPSG:4326').to_crs(3338).to_file(
    'data/derived/lookup_sales_report.geojson', driver='GeoJSON')

test = gpd.read_file('data/derived/lookup_sales_report.geojson')
test.explore()




# save GNIS incorporated places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/1/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/gnis_incorporated.geojson'
)
incorporated = gpd.read_file('data/raw/gnis_incorporated.geojson')
incorporated.explore()


# save GNIS unincorporated places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/2/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/gnis_unincorporated.geojson'
)
unincorporated = gpd.read_file('data/raw/gnis_unincorporated.geojson')
unincorporated.explore()

# save GNIS places data from USGS 
geo_save(
    geo_input = 'https://carto.nationalmap.gov/arcgis/rest/services/geonames/MapServer/3/query?outFields=*&where=state_alpha%3D%27AK%27&f=geojson',
    geo_output = 'data/raw/gnis_places.geojson'
)
places = gpd.read_file('data/raw/gnis_places.geojson')
places.explore()


tmp = places[places['gaz_name' == 'Aniak']]




# save ak_coastline to file from DNR
geo_save(
    geo_input = 'https://arcgis.dnr.alaska.gov/arcgis/rest/services/OpenData/Physical_AlaskaCoast/MapServer/1/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/alaska_coastline.geojson')

# save community locations from DCCED
geo_save(
    geo_input = 'https://maps.commerce.alaska.gov/server/rest/services/Community_Related/Community_Locations_and_Boundaries/MapServer/0/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/community_locations.geojson')

# save Electric North boundary (from .gitignored directory, downloaded from Google Drive) to file 
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_outline.shp',
    geo_output = 'data/raw/en_outline.geojson')

# save Electric North regional grids (from .gitignored directory, downloaded from Google Drive) to file
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_regionalGrids.shp',
    geo_output = 'data/raw/en_regional_grids.geojson')

# save Electric North regional grid capacity (from .gitignored directory, downloaded from Google Drive) to file
geo_save(
    geo_input = 'data/source/Shapefile_export/EN_regionalGrids_capacity.shp',
    geo_output = 'data/raw/en_regional_grids_capacity.geojson')

# save AETR generation data to file
(pd.read_csv('https://raw.githubusercontent.com/acep-uaf/aetr-web-book-2024/main/data/final_data/generation.csv')
    .dropna(subset=['generation'])
    .query('generation >= 0')
    .to_csv('data/derived/generation.csv'))


# run transmission line cleaning script
from src.pipeline.clean_aea_transmission_lines import voltage_cleaning

voltage_cleaning(
    input = 'data/source/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp',
    output = 'data/derived/transmission.geojson')



