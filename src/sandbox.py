import geopandas as gpd

# Set the path to your .gdb file
gdb_path = "data/raw/Alaska_population_locations.gdb"

# Open the .gdb file with geopandas (Note: only feature classes will be imported)
gdf = gpd.read_file(gdb_path)

# Print or process the GeoDataFrame
print(gdf.head())
