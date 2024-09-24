import geopandas as gpd

# pull interties
lookup_interties = gpd.read_file('data/raw/es_lookup_interties.csv')

# pull current interties
current_interties = lookup_interties[lookup_interties['Current ID'] == 'True']

# change Tooksook to Toksook


# pull intertie id and communities intertied, rename
communities = current_interties[['intertie_id', 'Communities Intertied']]
communities = communities.rename(columns={'Communities Intertied': 'community'})

# split on semi-colon and comma, explode out to more rows
communities['community'] = communities['community'].str.split(r'[;,]\s*')
communities_exploded = communities.explode('community')
# communities_exploded.rename(columns={'communities':'community'}, inplace=True)

# need id for each community (GNIS?)
# could have GNIS plus geometry

# write to file
communities_exploded.to_csv('data/derived/communities.csv')

