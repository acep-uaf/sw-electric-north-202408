import geopandas as gpd
import pandas as pd


gdf = gpd.read_file('data/raw/alaska_population_locations.geojson')
gdf.explore()



new_geometry = gpd.points_from_xy([1261269.7978444276] * len(gdf), [957469.3072573149] * len(gdf))
gdf['geometry'] = new_geometry



gdf.explore()


lines = gpd.read_file('data/derived/transmission.geojson')
lines.explore()

plants = gpd.read_file('data/derived/plant_locations.geojson')
plants.explore()



# try to join AETR generation with GNIS identifiers from ES workbooks
aetr_gen = gpd.read_file('data/derived/generation.csv')
aetr_names = aetr_gen[['plant_name', 'generation']]

plants = gpd.read_file('data/derived/plant_locations.geojson')
plant_geoms = plants[['plant_name', 'geometry']]

test = plant_geoms.merge(aetr_names, on='plant_name')

outer = plant_geoms.merge(aetr_names, how='outer', indicator=True)
test = outer[outer['_merge'] == 'left_only']

outer['_merge'] = (outer['_merge']
                    .cat.rename_categories({'left_only':'es_plants', 'right_only':'aetr_gen'}))

outer = outer.sort_values(by = '_merge')

outer.to_file('data/derived/plant_location_merge_debugging.geojson', driver = 'GeoJSON')