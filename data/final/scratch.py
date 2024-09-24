import geopandas as gpd

# start with places polygons
places = gpd.read_file('data/raw/ak-dol.places2020/data/ak-dol.places2020.geojson')

m = places.explore(
    color='blue'
)

# add transmission lines
lines = gpd.read_file('data/derived/transmission/transmission.geojson')

lines.explore(
    m=m, 
    color='red'
)

# add more data
plants = gpd.read_file('data/derived/plants/plants.geojson')

plants.explore(
    m=m,
    color = 'orange'
)



test = gpd.read_file('data/raw/es/data/es_lookup_sales_report.geojson')
test.explore(
    m=m, 
    color='black'
)
                                                                          