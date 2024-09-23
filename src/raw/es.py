import pandas as pd
import geopandas as gpd


from src.raw.functions.api_xlsx import xlsx_url_to_file
from src.raw.functions.api_geo import geo_save


### Infrastructure Workbook

# download infrastructure xlsx from Energy Stats Github repo, save to file

xlsx_url_to_file(
    xlsx_url = 'https://raw.githubusercontent.com/acep-uaf/ak-energy-statistics-2011_2021/main/workbooks/Energy_Stats_Infrastructure_2021.xlsx', 
    file = 'data/raw/Energy_Stats_Infrastructure_2021.xlsx')


# pull plant locations, save as geojson
df = pd.read_excel(
        'data/raw/Energy_Stats_Infrastructure_2021.xlsx',
        sheet_name = 'LOOKUP PLANTS 2023-11-13')

gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.Latitude), crs='EPSG:4326').to_crs(3338).to_file(
    'data/raw/es_lookup_plants.geojson', driver='GeoJSON')



# pull intertie lookup, save as geojson
df = pd.read_excel(
        'data/raw/Energy_Stats_Infrastructure_2021.xlsx',
        sheet_name = 'LOOKUP INTERTIES 2023-11-08')

df.to_csv('data/raw/es_lookup_interties.csv', index=False)




### Generation Workbook

# download generation xlsx from Energy Stats Github repo, save to file
xlsx_url_to_file(
    xlsx_url = 'https://github.com/acep-uaf/ak-energy-statistics-2011_2021/raw/main/workbooks/Energy_Stats_Generation_Tables.xlsx', 
    file = 'data/raw/Energy_Stats_Generation_Tables.xlsx')


# pull sales reporting data from generation xlsx, save to file
df = pd.read_excel(
        'data/raw/Energy_Stats_Generation_Tables.xlsx',
        sheet_name = 'LOOKUP SalesReport 2023-11-13')

(gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs='EPSG:4326')
    .to_crs(3338)
    .to_file('data/raw/es_lookup_sales_report.geojson', driver='GeoJSON'))

# test = gpd.read_file('data/derived/lookup_sales_report.geojson')


# pull annual operations data from generation xlsx, save to file
df = pd.read_excel(
        'data/raw/Energy_Stats_Generation_Tables.xlsx',
        sheet_name = 'AnnualOperationsData 2023-11-13')

df.to_csv('data/raw/es_annual_operations.csv', index=False)



# pull monthly gen data from generation xlsx, save to file
df = pd.read_excel(
        'data/raw/Energy_Stats_Generation_Tables.xlsx',
        sheet_name = 'Monthly Gen 2001-2021')

df.to_csv('data/raw/es_monthly_gen.csv', index=False)



# pull data from generation xlsx, save to file
df = pd.read_excel(
        'data/raw/Energy_Stats_Generation_Tables.xlsx',
        sheet_name = 'All Gen FUEL TYPE PIVOT',
        skiprows=4,
        skipfooter=1).rename(columns={'Row Labels': 'Year'})



df.to_csv('data/raw/es_gen_fuel_type.csv', index=False)
