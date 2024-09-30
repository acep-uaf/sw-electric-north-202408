import ibis
ibis.options.interactive = True

# create empty database
con = ibis.duckdb.connect('data/final/db/test.ddb')
con.load_extension('spatial')

# write communities into db (geospatial!!)
communities = con.read_geo(table_name='communities', source='data/derived/communities/communities.geojson')

# generation into db
generation = con.read_csv(table_name='generation', source_list='data/derived/generation/generation.csv')

# interties
interties = con.read_csv(table_name='interties', source_list='data/derived/interties/interties.csv')

# plants
plants = con.read_csv(table_name='plants', source_list='data/derived/plants/plants.csv')

# transmission
transmission = con.read_geo(table_name= 'transmission', source='data/derived/transmission/transmission.geojson')


con.list_tables()

generation
communities

con.disconnect()
