import pandas as pd
import geopandas as gpd

from fuzzywuzzy import fuzz, process

# import dataframe of cannonical names
pl = gpd.read_file('data/raw/usgs/data/usgs_places.geojson')
canonical_df = pl[['gaz_name']].drop_duplicates().rename(columns={'gaz_name':'Canonical Name'})


# import dataframe of uncleaned names
op = pd.read_csv('data/raw/es/data/us_annual_operations.csv')
uncleaned_df = op[['AEA Reporter Name']].drop_duplicates().rename(columns={'AEA Reporter Name':'Uncleaned Name'})


# merge direct matches
matches = canonical_df.merge(uncleaned_df[['Uncleaned Name']], left_on='Canonical Name', right_on='Uncleaned Name', how='inner')
matches = matches.drop_duplicates(subset='Uncleaned Name', keep=False)

# add column for fuzzymatches without direct match
uncleaned_df['Canonical Match'] = None

# Loop and fuzzymatch uncleaned names with cutoff threshold
for index, row in uncleaned_df.iterrows():
    if pd.isnull(row['Canonical Match']):
        matches = process.extractOne(row['Uncleaned Name'], canonical_df['Canonical Name'])
        if matches[1] > 89: # Change the cutoff value to your liking
            uncleaned_df.at[index, 'Canonical Match'] = matches[0]




# Write entire dataframe to file
uncleaned_df.to_csv('output.csv', index=False)

test = pd.read_csv('output.csv')


test = p.merge(o, how='outer', indicator=True)


for record in o.name:
    process.extractOne(record, p.name)

for index, record in o.iterrows():
    match = fuzz.ratio(record['name'], p.name)
    if match:
        o.at[index, 'canonical'] = match[0]


# import dataframe of cannonical names
# import dataframe of uncleaned names

# look for direct match, uncleaned to cannonical
    # if no direct match
        # loop and fuzzymatch with cutoff threshold
    # if fuzzymatched
        # append new record with cannonical and new alias
    # if no fuzzymatch
        # append new record with NO cannonical and new alias?
# write the whole mess to file 




# import dataframe of cannonical names
# import dataframe of uncleaned names

# look for direct match, uncleaned to cannonical
    # if no direct match
        # loop and fuzzymatch with cutoff threshold
    # if fuzzymatched
        # append new record with cannonical and new alias
    # if no fuzzymatch
        # append new record with NO cannonical and new alias?
# write the whole mess to file 


