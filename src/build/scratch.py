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
aetr_names = aetr_gen[['plant_name', 'acep_region']].drop_duplicates(keep='first')

plants = gpd.read_file('data/derived/lookup_plants.geojson')
plant_ids = plants[['plant_name', 'AEA Plant ID']].drop_duplicates(keep='first')

test = plant_ids.merge(aetr_names, on='plant_name')

outer = plant_ids.merge(aetr_names, how='outer', indicator=True)
test = outer[outer['_merge'] == 'left_only']

outer['_merge'] = (outer['_merge']
                    .cat.rename_categories({'left_only':'lookup_plants_only', 'right_only':'aetr_gen_only'}))

outer = outer.sort_values(by = '_merge')

outer.to_csv('data/derived/aetr_es_merge_debugging.csv')


