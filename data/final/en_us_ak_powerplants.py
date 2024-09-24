import geopandas as gpd

derived_plants = gpd.read_file('data/raw/es/data/es_lookup_plants.geojson')

derived_plants.rename(columns={
    'AEA Plant ID' : 'aea_id',
    'eia_plant_id' : 'eia_id',
    'nameplate_capacity' : 'capacity_mw',
    'Latitude' : 'latitude'
    },
    inplace=True
)

plants = derived_plants[[
    'aea_id', 
    'eia_id', 
    'plant_name', 
    'AEA_operator Id',
    'eia_operator_id',
    'capacity_mw',
    'latitude',
    'longitude',
    'geometry']]


# need primary fuel, other fuel
gen_fuel_type = gpd.read_file('data/raw/es/data/es_gen_fuel_type.csv')




plants.to_file('data/final/en_us_ak_powerplants.geojson')
load = gpd.read_file('data/final/en_us_ak_powerplants.geojson')
load.explore()


