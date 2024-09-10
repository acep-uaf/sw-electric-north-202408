
from src.pipeline.api_xlsx import xlsx_url_to_file




xlsx_url = 'https://raw.githubusercontent.com/acep-uaf/ak-energy-statistics-2011_2021/main/workbooks/Energy_Stats_Infrastructure_2021.xlsx'
file = 'data/raw/Energy_Stats_Infrastructure_2021.xlsx'

xlsx_url_to_file(url = xlsx_url, file = file)
