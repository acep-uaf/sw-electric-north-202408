import geopandas as gpd

raw_coastline = gpd.read_file('data/raw/dnr/data/dnr_coastline.geojson')

coastline = raw_coastline.cx[0:-180 , :]
coastline_3338 = coastline.to_crs(3338)

coastline_3338.to_file('data/derived/coastline/coastline.geojson', driver = "GeoJSON")
