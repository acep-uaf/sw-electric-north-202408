import pandas as pd

# load data
infrastructure = pd.read_csv('data/raw/es/data/es_infrastructure.csv')

infrastructure.rename(inplace=True, columns={
    'AEA plant ID': 'aea_plant_id',
    'Plant Name': 'plant_name',
    'Intertie ID': 'intertie_id',
    'Generator ID': 'generator_id',
    'Prime Mover': 'prime_mover',
    'Nameplate Capacity (MW)': 'nameplate_capacity_mw',
    'Planned or Actual Retirement Year': 'planned_or_actual_retirement_year',
    'Status': 'status'
})

out = infrastructure[[
    'aea_plant_id',
    'plant_name',
    'intertie_id',
    'generator_id',
    'prime_mover',
    'nameplate_capacity_mw',
    'status'
]]

# add intertie_id to mcroberts creek (railbelt, 215-2015)
out.loc[out.aea_plant_id == 'P276', 'intertie_id'] = '215-1985'

out.to_csv('data/derived/infrastructure/infrastructure.csv', index=False)
