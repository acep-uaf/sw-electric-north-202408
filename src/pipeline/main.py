import geopandas as gpd


from src.pipeline.api_xlsx import xlsx_url_to_file

# download xlsx from Energy Stats Github repo, save to file
xlsx_url_to_file(
    url = 'https://raw.githubusercontent.com/acep-uaf/ak-energy-statistics-2011_2021/main/workbooks/Energy_Stats_Infrastructure_2021.xlsx', 
    file = 'data/raw/Energy_Stats_Infrastructure_2021.xlsx'
)


# run transmission line cleaning script
from src.pipeline import clean_aea_transmission_lines

clean_aea_transmission_lines()
