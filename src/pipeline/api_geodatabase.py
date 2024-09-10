import geopandas as gpd

# define path
gdb_path = "data/raw/Alaska_population_locations.gdb.zip"

# open geodatabase
target_database = gpd.read_file(gdb_path)

# print head to check
print(target_database.head())
