import geopandas as gpd
import pandas as pd

# load points
# load polys with population data
# load fips to intertie lookup data
points = gpd.read_file('data/raw/census_2024_gaz_places.geojson')
polys = gpd.read_file('data/derived/communities.geojson')
lookup = pd.read_csv('data/derived/lookup_fips_interties.csv')


# pull id and point data from census gazateer points
id_points = points[[
    'geoid',
    'ansi_code',
    'latitude',
    'longitude'
]]

# rename geoid to fips
id_points.rename(inplace=True, columns={
    'geoid': 'fips'
})

# drop geometry from ak dol polygons
poly_minus_geom = polys.drop(columns={
    'geometry'
})

poly_minus_geom['fips'] = pd.to_numeric(poly_minus_geom['fips'])

# add point geometry to ak dol data (stripped of geometry)
merged = pd.merge(poly_minus_geom, id_points, how='left', on='fips')

# convert to geodataframe, define crs
gdf = gpd.GeoDataFrame(merged, geometry=gpd.points_from_xy(merged.longitude, merged.latitude), crs="EPSG:4326"
).to_crs(3338)

# write to file
gdf.to_file('data/derived/community_points.geojson', driver='GeoJSON')
