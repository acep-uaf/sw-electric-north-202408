import geopandas as gpd

def geo_save(geo_input, geo_output, driver='GeoJSON', crs=None):
    gdf = gpd.read_file(geo_input)
        
    if crs is not None:
        reprojected_gdf = gdf.to_crs(crs)
    else:
        reprojected_gdf = gdf  # keep the original crs if none provided
    
    reprojected_gdf.to_file(geo_output, driver=driver)

if __name__ == "__main__":
    geo_save()




