import yaml
import pandas as pd
import geopandas as gpd
from fuzzywuzzy import process



def make_yaml(df_path, id_column: str, name_column: str, yaml_path):
    # read file
    df = gpd.read_file(df_path)

    # # select column of names
    # c = df[[id_column, name_column]]
    # # make dictionary of names with empty alias
    # dict = c.to_dict()

    d = df.set_index(id_column)[name_column].to_dict()

    # yaml.dump({k: {'name': v} for k, v in d.items()}, open(yaml_path, 'w'), default_flow_style=False)
    yaml.dump({k: {'name': v, 'alias': None} for k, v in d.items()}, open(yaml_path, 'w'), default_flow_style=False)


    # # write to file as yaml
    # with open(yaml_path, 'w') as outfile:
    #     yaml.dump(d, outfile, default_flow_style=False)

df_path = 'data/raw/usgs_places.geojson'
id_column = 'gaz_id'
name_column = 'gaz_name'
yaml_path = 'data/derived/crosswalk_communities.yaml'

make_yaml(df_path, id_column, name_column, yaml_path)











def add_alias(df_path, name_column: str, yaml_path):
    # import yaml of aliases as dictionary
    with open(yaml_path) as f:
        aka = yaml.safe_load(f)
    # import dataframe with uncleaned names
    df = gpd.read_file(df_path)
    # pull name column from uncleaned dataframe, rename, make dictionary
    names = df[name_column].rename('name').to_dict()

    # fuzzy match to dictionary of standardized names (for loop)
    for community in names.values():
        print(community)


    for alias in aka.values():
        print(alias)

    # add matched names as aliases to dictionary of standardized names (for loop)
    # new_aliases = ['Utqiagvik (formerly Barrow)', 'City of Utqiagvik']
    # for community in aka['communities']:
    #     community['aliases'].extend(new_aliases)


    # write to file dictionary of standardized names
    with open(yaml_path, 'w') as outfile:
        yaml.dump(aka['communities'], outfile, default_flow_style=False)
    return(aka)


df_path = 'data/raw/usgs_places.geojson'
name_column = 'gaz_name'
yaml_path = 'data/derived/crosswalk_communities.yaml'

add_alias(df_path, name_column, yaml_path)



def standardize_names(df, name_column: str, yaml_path: str, output_file: str):
    # import yaml of aliases as dictionary
    # import dataframe with uncleaned names
    # loop through alias dictionary for matching aliases, overwrite
    # save dataframe to file, different location













# fake generation data
g = {'town': ['Utqiagvik', 'Craig', 'Sitka', 'Petersburg', 'Kake'], 
    'generation': [1000, 300, 400, 300, 200] }
gen = pd.DataFrame(data=g)

# fake capacity data
c = {'town': ['Barrow', 'City of Craig', 'Sitka Borough', 'Petersburg', 'Kake'], 
    'capacity': [3, 4, 2, 3, 1]}
cap = pd.DataFrame(data=c)

join = cap.merge(gen, on='town')

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
