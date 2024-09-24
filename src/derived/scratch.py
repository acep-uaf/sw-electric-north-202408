import geopandas as gpd

# start with places polygons
places = gpd.read_file('data/source/ak-dol.places2020/data/ak-dol.places2020.geojson')

m = places.explore(
    color='blue'
)

# add transmission lines
lines = gpd.read_file('data/derived/transmission.geojson')

lines.explore(
    m=m, 
    color='red'
)

# add more data
plants = gpd.read_file('data/derived/plants.geojson')

plants.explore(
    m=m,
    color = 'red'
)



test = gpd.read_file('data/raw/es_lookup_sales_report.geojson')
test.explore(
    m=m, 
    color='black'
)
                                                                          