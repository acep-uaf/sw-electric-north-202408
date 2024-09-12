import geopandas as gpd


gdf = gpd.read_file('data/raw/alaska_population_locations.geojson')
gdf.explore()



new_geometry = gpd.points_from_xy([1261269.7978444276] * len(gdf), [957469.3072573149] * len(gdf))
gdf['geometry'] = new_geometry



gdf.explore()


lines = gpd.read_file('data/derived/transmission.geojson')
lines.explore()

plants = gpd.read_file('data/derived/plant_locations.geojson')
plants.explore()
