import pandas as pd

infrastructure = pd.read_csv('data/derived/infrastructure/infrastructure.csv')


# filter out retired plants (RE) and long-term out-of-serveice plants (OS)
active_codes = ['OP', 'SB', 'OA'] # operational (OP), standby (SB), temporary out-of-service (OA)
infrastructure = infrastructure[infrastructure['status'].isin(active_codes)]

# aggregate for total capacity by intertie
sum_capacity = infrastructure.groupby(['intertie_id'])['nameplate_capacity_mw'].sum().reset_index(
).rename(columns={'nameplate_capacity_mw': 'sum_capacity_mw'})

# define the list of renewable sources
renewable_sources = ['HY', 'PV', 'WT'] # hydro, photovoltaic, wind turbine

# sum renewable generation by intertie
renewable_capacity = infrastructure.loc[
    (infrastructure['prime_mover'].isin(renewable_sources)), 
    ['intertie_id', 'nameplate_capacity_mw']
].groupby('intertie_id')['nameplate_capacity_mw'].sum().reset_index(
).rename(columns={'nameplate_capacity_mw': 'renewable_capacity_mw'})

# merge total capacity with renewable capacity, set na's equal to 0 (inerties without renewables)
renewable_ratio = pd.merge(sum_capacity, renewable_capacity, how='left', on='intertie_id').fillna(0)

renewable_ratio['renewable_ratio'] = renewable_ratio['renewable_capacity_mw']/renewable_ratio['sum_capacity_mw']

out = renewable_ratio

out.to_csv('data/final/data/renewable_capacity.csv')