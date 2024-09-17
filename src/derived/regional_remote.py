import geopandas as gpd

points = gpd.read_file('data/raw/dcced_communities.geojson')
polys = gpd.read_file('data/raw/en_regional_grids.geojson')

coast = gpd.read_file('data/raw/dnr_coastline.geojson')
coast.plot()

regional = points[points.intersects(polys.geometry)]

regional.explore()


ax = points.plot(color='black')
polys.plot()
polys.explore()
