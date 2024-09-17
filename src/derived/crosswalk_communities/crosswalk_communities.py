import yaml
import pandas as pd
import geopandas as gpd



def make_yaml(df_path, column_name:str):
    # read file
    df = gpd.read_file(df_path)
    # select column of names
    c = df[[column_name]]
    # construct dictionary of names with empty alias
    dict = c.to_dict()
    yaml_string = yaml.dump(dict)
    print(yaml_string, 'test.yaml')
    # write to file as yaml

df_path = 'data/raw/dcced_communities.geojson'

make_yaml(df_path, 'CommunityName')








def add_alias(yaml_file):
    # import yaml of aliases
    with open(yaml_file) as f:
        aka = yaml.safe_load(f)
    return(aka)

add_alias('src/derived/crosswalk_communities/crosswalk.yaml')


for community in aka['communities']: 
    print(community)

join = cap.merge(gen, on='town')










# fake generation data
g = {'town': ['Utqiagvik', 'Craig', 'Sitka', 'Petersburg', 'Kake'], 
    'generation': [1000, 300, 400, 300, 200] }
gen = pd.DataFrame(data=g)

# fake capacity data
c = {'town': ['Barrow', 'City of Craig', 'Sitka Borough', 'Petersburg', 'Kake'], 
    'capacity': [3, 4, 2, 3, 1]}
cap = pd.DataFrame(data=c)



coast = gpd.read_file('data/derived/coastline.geojson')
coast.explore()


# Yaml target
# canonical community name:
# - alias
# - alias
# - alias
# other canonical community name:
# - alias
# - alias