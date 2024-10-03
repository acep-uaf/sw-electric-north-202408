import geopandas as gpd

read = gpd.read_file('data/raw/cares_boundary.geojson')

out = read

out.to_file('data/final/en_us_ak_boundary.geojson')