import geopandas as gpd

def geo_save(geo_input, geo_output):
    gpd.read_file(geo_input).to_file(geo_output, driver = 'GeoJSON')

if __name__ == "__main__":
    geo_save()
