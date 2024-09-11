

# download xlsx from Energy Stats Github repo, save to file
from src.pipeline.api_xlsx import xlsx_url_to_file

xlsx_url_to_file(
    xlsx_url = 'https://raw.githubusercontent.com/acep-uaf/ak-energy-statistics-2011_2021/main/workbooks/Energy_Stats_Infrastructure_2021.xlsx', 
    file = 'data/raw/Energy_Stats_Infrastructure_2021.xlsx'
)



# run transmission line cleaning script
from src.pipeline.clean_aea_transmission_lines import cleaning

cleaning(
    input = 'data/raw/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp',
    output = 'data/derived/aea_transmission_lines.geojson'
)



# save geodatabase to file as geojson
from src.pipeline.api_geo import geo_save

geo_save(
    geo_input = 'data/raw/Alaska_population_locations.gdb.zip',
    geo_output = 'data/raw/alaska_population_locations.geojson'
)

# save ak_coastline to file
geo_save(
    geo_input = 'https://arcgis.dnr.alaska.gov/arcgis/rest/services/OpenData/Physical_AlaskaCoast/MapServer/1/query?outFields=*&where=1%3D1&f=geojson',
    geo_output = 'data/raw/alaska_coastline.geojson'
)

# save Electric North boundary to file
geo_save(
    geo_input = 'data/raw/Shapefile_export/EN_outline.shp',
    geo_output = 'data/raw/en_outline.geojson'
)

# save Electric North regional grids to file
geo_save(
    geo_input = 'data/raw/Shapefile_export/EN_regionalGrids.shp',
    geo_output = 'data/raw/en_regional_grids.geojson'
)

# save Electric North regional grid capacity to file
geo_save(
    geo_input = 'data/raw/Shapefile_export/EN_regionalGrids_capacity.shp',
    geo_output = 'data/raw/en_regional_grids_capacity.geojson'
)
