import geopandas as gpd

def geo_save(geo_input, geo_output, driver = 'GeoJSON'):
    (gpd.read_file(geo_input)
    .to_crs(3338)
    .to_file(geo_output, driver = driver)
    )

if __name__ == "__main__":
    geo_save()





