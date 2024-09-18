import yaml
import pandas as pd
import geopandas as gpd
from fuzzywuzzy import process



# def make_yaml(df_path, id_column: str, name_column: str, yaml_path):
#     # read file
#     df = gpd.read_file(df_path)
#     # select columns of id and name, make dictionary
#     d = df.set_index(id_column)[name_column].to_dict()
#     # make empty key:value for alias, write to file
#     yaml.dump({k: {'name': v, 'alias': None} for k, v in d.items()}, open(yaml_path, 'w'), default_flow_style=False)


def make_yaml(df_path, name_column: str, id_column: str, yaml_path):
    df = gpd.read_file(df_path)   # read file

    d = df[[name_column, id_column]]   # select name and id columns

    # d.loc[:, 'alias'] = ''   # create empty column alias

    # d.columns = [{'name': name_column, 'gnis': id_column, 'alias': 'alias'}]   # rename columns

    d.set_index(name_column, inplace=True)

    # Create a dictionary from the DataFrame
    mapping = d.to_dict(orient='series')

    # Write the dictionary to YAML
    yaml.dump(mapping, open(yaml_path, 'w'), default_flow_style=False)

df_path = 'data/raw/usgs_places.geojson'
id_column = 'gaz_id'
name_column = 'gaz_name'
yaml_path = 'data/derived/crosswalk_communities.yaml'

make_yaml(df_path, id_column, name_column, yaml_path)


canonical_name:
- alias
- alias
- alias


df.new_unclean_name


canonical_name, alias
canonical_name, alias2
canonical_name, alias3





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
