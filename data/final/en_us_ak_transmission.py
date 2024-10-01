import geopandas as gpd

transmission = gpd.read_file('data/derived/transmission/transmission.geojson')

transmission.explore()

transmission.to_file('data/final/data/en_us_ak_transmission.geojson', driver='GeoJSON')
