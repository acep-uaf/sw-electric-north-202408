import geopandas as gpd


db = gpd.read_file('data/raw/alaska_population_locations.geojson')
db.explore()

template = db[:1]

template.explore()

template.to_file('data/final/template.geojson')
