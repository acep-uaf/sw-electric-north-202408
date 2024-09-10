import geopandas as gpd

def gdb_to_geojson(gdb_input, geojson_output):
    gpd.read_file(gdb_input).to_file(geojson_output, driver = 'GeoJSON')

if __name__ == "__main__":
    gdb_to_geojson()
