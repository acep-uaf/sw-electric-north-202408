import pandas as pd
import geopandas as gpd

# want:
# plant_id
# intertie_id
# other ids (aea, eia)
# plant_name
# capacity
# prime_mover (lookup?)
# lat/long


# load data
plants = gpd.read_file('data/raw/es/data/es_lookup_plants.geojson')
infrastructure = pd.read_csv('data/derived/infrastructure/infrastructure.csv')


# drop empty columns, read as 'Unnamed: 0' etc
plants.drop(list(plants.filter(regex='Unnamed')), axis=1, inplace=True)

# rename a bunch of columns
plants.rename(inplace=True, columns={
    'AEA Plant ID':'aea_plant_id',
    'PCE reporting ID':'pce_reporting_id',
    'AEA_operator Id':'aea_operator_id',
    'INTERTIE_Current Intertie ID':'intertie_id',
    'INTERTIE_Current Intertie name':'current_intertie_name',
    'Currently Reports to EIA':'eia_reporting',
    'Currently Reports to PCE':'pce_reporting',
    'nameplate_capacity':'capacity_mw',
    'OPERATOR_Operator_name':'operator_name',
    'OPERATOR_sector__id':'operator_sector_id',
    'OPERATOR_sector__name':'operator_sector_name',
    'OPERATOR_sector__number':'operator_sector_number',
    'Primary voltage':'primary_voltage',
    'Primary voltage 2':'primary_voltage_2',
    'Phases':'phases',
    'Latitude':'latitude',
    'status (OP, SB, OA)':'status',
    'Notes':'notes'})

# drop operator name, intertie name (helps normalize the database)
plants.drop(inplace=True, columns={
    'operator_name', 
    'current_intertie_name', 
    'operator_sector_name'})


plants_coords = plants[[
    'aea_plant_id',
    'latitude',
    'longitude',
    'geometry'    
]]



# add infrastructure data
# select operational (or temporarily out of service)
active_codes = ['OP', 'SB', 'OA']
infrastructure = infrastructure[infrastructure['status'].isin(active_codes)]


infra_coords = infrastructure.merge(plants_coords, on='aea_plant_id')

aggregated = infra_coords.groupby([
    'aea_plant_id', 
    'plant_name',
    'intertie_id',
    'primary_fuel',
    'other_fuel',
    'latitude',
    'longitude',
    'geometry'
], dropna=False)['nameplate_capacity_mw'].sum().reset_index()


out_pd = aggregated[[
    'aea_plant_id', 
    'plant_name',
    'intertie_id',
    'primary_fuel',
    'other_fuel',
    'nameplate_capacity_mw',
    'latitude',
    'longitude',
    'geometry'
]]


out = gpd.GeoDataFrame(out_pd, geometry='geometry').to_crs(3338)


out.to_file('data/derived/plants/plants.geojson')

