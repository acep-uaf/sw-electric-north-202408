import geopandas as gpd
import pandas as pd
import requests

from src.pipeline.api_xlsx import xlsx_url_to_file

# download xlsx from Energy Stats Github repo, save to file
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


from src.pipeline.clean_geodatabase import gdb_to_geojson

gdb_to_geojson(
    gdb_input = 'data/raw/Alaska_population_locations.gdb.zip',
    geojson_output = 'data/derived/alaska_population_locations.geojson'
)
