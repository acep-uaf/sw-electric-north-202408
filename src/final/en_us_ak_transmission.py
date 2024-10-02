import geopandas as gpd

transmission = gpd.read_file('data/derived/transmission.geojson')

transmission.explore()

transmission.to_file('data/final/en_us_ak_transmission.geojson', driver='GeoJSON')
