import restapi
import geopandas as gpd
import matplotlib.pyplot as plt


# full URL with service, layer, and query
# https://arcgis.dnr.alaska.gov/arcgis/rest/services/OpenData/Physical_AlaskaCoast/MapServer/1/query?outFields=*&where=1%3D1&f=geojson

# connect to server
rest_url = 'https://arcgis.dnr.alaska.gov/arcgis/rest/services/'
ags = restapi.ArcServer(rest_url)


# print list of folders and services
for root, services in ags.walk():
    print('Folder: {}'.format(root))
    print('Services: {}\n'.format(services))


# pull service
Physical_AlaskaCoast = ags.getService('OpenData/Physical_AlaskaCoast/MapServer')
# pull layer
Coast = Physical_AlaskaCoast.layer('Alaska 1:250,000')
# set query parameters
params = {'f': 'geojson'}  # return GeoJSON format


# query! (takes a second)
featureSet = Coast.query(params=params)


# convert to geopandas geodataframe
gdf = gpd.GeoDataFrame.from_features(featureSet.features)
# set the CRS (Alaskan Albers)
gdf = gdf.set_crs('epsg:3338')

gdf.plot()

# write to file
gdf.to_file('alaska_coast.geojson', driver='GeoJSON')
