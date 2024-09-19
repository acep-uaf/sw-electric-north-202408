import geopandas as gpd

transmission = gpd.read_file('data/derived/transmission.geojson')
transmission.explore()

buffer_dist = 10000   # buffer distance in meters

buffered = transmission.buffer(buffer_dist).envelope
buffered.explore()
