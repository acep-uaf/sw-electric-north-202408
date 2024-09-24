import geopandas as gpd

# load data
plants = gpd.read_file('data/raw/es_lookup_plants.geojson')

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


# awful code, but gets the job done
plants.rename(inplace=True, columns={'intertie_id':'intertie_id_copy'})
plants.insert(0, 'intertie_id', plants['intertie_id_copy'])
plants.drop(inplace=True, columns={'intertie_id_copy'})

plants.to_file('data/derived/plants.geojson')


# need generation by fuel type (from AETR?)
