import pandas as pd

# want:
#
#     plant_id,
#     year,
#     month,


aetr_gen = pd.read_csv('data/raw/aetr/data/aetr_generation.csv')
lookup = pd.read_csv('data/derived/lookup_plant_name_id/lookup_plant_name_id.csv')


merged = pd.merge(aetr_gen, lookup, how='left', on='plant_name').drop_duplicates()

out = merged[[
    'aea_plant_id',
    'year',
    'fuel_type',
    'generation'
]]


out.to_csv('data/derived/generation/generation.csv', index=False)

load = pd.read_csv('data/derived/generation/generation.csv')
