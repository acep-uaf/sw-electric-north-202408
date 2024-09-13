import geopandas as gpd
import pandas as pd


gdf = gpd.read_file('data/raw/alaska_population_locations.geojson')
gdf.explore()



new_geometry = gpd.points_from_xy([1261269.7978444276] * len(gdf), [957469.3072573149] * len(gdf))
gdf['geometry'] = new_geometry



gdf.explore()






# try to join AETR generation with GNIS identifiers from ES workbooks
aetr_gen = gpd.read_file('data/derived/generation.csv')
aetr_names = aetr_gen[['plant_name', 'acep_region']].drop_duplicates(keep='first')

es_ops = gpd.read_file('data/derived/annual_operations.csv')
es_ops_ids = (es_ops[['AEA Reporter Name', 'AEA Reporter ID']].drop_duplicates(keep='first')
                .rename(columns={'AEA Reporter Name': 'plant_name'}))

test = es_ops_ids.merge(aetr_names, on='plant_name')

outer = es_ops_ids.merge(aetr_names, how='outer', indicator=True)
test = outer[outer['_merge'] == 'left_only']

outer['_merge'] = (outer['_merge']
                    .cat.rename_categories({'left_only':'annual_ops_only', 'right_only':'aetr_gen_only'}))

outer = outer.sort_values(by = '_merge')

outer.to_csv('data/derived/aetr_es_merge_debugging.csv')


both = outer['_merge'].str.count('both')

outer['_merge'].value_counts()


len(set(aetr_gen["plant_name"]))
len(set(es_ops["AEA Reporter Name"]))


(set(aetr_gen["plant_name"]) | set(es_ops["AEA Reporter Name"])).symmetric_difference(outer["plant_name"])
