import pandas as pd

raw_plants = pd.read_excel(
    'data/raw/Energy_Stats_Infrastructure_2021.xlsx',
    sheet_name = 'LOOKUP PLANTS 2023-11-13')



raw_plants.to_csv('data/derived/plant_locations.csv')
