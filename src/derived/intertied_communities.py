import pandas as pd

lookup_interties = pd.read_csv('data/derived/lookup_interties.csv')

# pull current interties
current_interties = lookup_interties[lookup_interties['Current ID'] == True]

# change Tooksook to Toksook

# pull intertie id and communities intertied
id_communities = current_interties[['intertie_id', 'Communities Intertied']]

id_communities = id_communities.rename(columns={'Communities Intertied': 'communities'})

id_communities['communities'] = id_communities['communities'].str.split(r'[;,]\s*')
id_communities_exploded = id_communities.explode('communities')


id_communities_exploded.to_csv('data/derived/intertied_communities.csv')
