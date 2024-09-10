import geopandas as gpd

# define path
geodatabase_path = "data/raw/Alaska_population_locations.gdb.zip"

# open geodatabase
target_database = gpd.read_file(geodatabase_path)

# print head to check
print(target_database.head())
