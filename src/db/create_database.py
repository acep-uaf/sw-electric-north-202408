import ibis
ibis.options.interactive = True

# create empty database
con = ibis.connect("duckdb://data/db/test.ddb")
con.load_extension('spatial')

con.list_tables()

# write communities into db (geospatial!!)
con.create_table(
    'communities', 
    con.read_geo(table_name='communities', source='data/derived/communities.geojson'),
    overwrite=True
)

# generation into db
con.create_table(
    'generation', 
    con.read_csv(table_name='generation', source_list='data/derived/generation.csv'),
    overwrite=True)

# interties
con.create_table(
    'interties', 
    con.read_csv(table_name='interties', source_list='data/derived/interties.csv'),
    overwrite=True
)

# plants
con.create_table(
    'plants', 
    con.read_csv(table_name='plants', source_list='data/derived/plants.geojson'),
    overwrite=True
)

# transmission
con.create_table(
    'transmission', 
    con.read_geo(table_name= 'transmission', source='data/derived/transmission.geojson'),
    overwrite=True
)


con.list_tables()
con.disconnect()
