import ibis
from ibis import _

ibis.options.interactive = True

con = ibis.connect("duckdb://data/db/raw.ddb")
con.load_extension('spatial')

con.list_tables()




# out = test.filter(_.county_name == 'Nome')

# pan = out.to_pandas()
# pan.crs = 'EPSG:3338'

# pan.explore()


con.list_tables()

con.disconnect()
