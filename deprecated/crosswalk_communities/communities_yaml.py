import yaml
import geopandas as gpd

com = gpd.read_file('data/raw/dcced/data/dcced_communities.geojson')
com.explore()

# Define a dictionary that maps the current column names to their desired new names for renaming
column_renames = {
    'OBJECTID': 'id',
    'CommunityName': 'community',
    'CommunityTypeName': 'type'
}

df = (com[['OBJECTID', 'CommunityName', 'CommunityTypeName']]
        .rename(columns=column_renames)
        .assign(other_names='NA'))



# df = com[['OBJECTID', 'CommunityName', 'CommunityTypeName', 'CommunityAreaTypeName']]

test = yaml.dump(df.to_dict(orient='records'),default_flow_style=None)

with open('data/derived/crosswalk_communities/communities.yaml', 'w') as file:
    documents = yaml.dump({'result': df.to_dict(orient='records')}, file, default_flow_style=False)


