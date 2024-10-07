import geopandas as gpd
import pyogrio

com = gpd.read_file('data/final/en_us_ak_communities.geojson')

com.to_file('data/final/test.gdb', driver='OpenFileGDB')


gdb = gpd.read_file('data/raw/en_population_locations.geojson')
