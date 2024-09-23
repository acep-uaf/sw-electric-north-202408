import pandas as pd

# pull interties
lookup_interties = pd.read_csv('data/raw/es_lookup_interties.csv')

# pull current interties
current_interties = lookup_interties[lookup_interties['Current ID'] == True]

# change Tooksook to Toksook


# pull intertie id and communities intertied, rename
id_communities = current_interties[['intertie_id', 'Communities Intertied']]
id_communities = id_communities.rename(columns={'Communities Intertied': 'communities'})

# split on semi-colon and comma, explode out to more rows
id_communities['communities'] = id_communities['communities'].str.split(r'[;,]\s*')
id_communities_exploded = id_communities.explode('communities')
id_communities_exploded.rename(columns={'communities':'community'}, inplace=True)

# need id for each community (GNIS?)
# could have GNIS plus geometry

# write to file
id_communities_exploded.to_csv('data/derived/intertied_communities.csv')
