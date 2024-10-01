import pandas as pd
import geopandas as gpd

# community population info from 2020 census, use generation and capacity numbers from 2020
# unfortunately our capacity data is from 2023, fix later

# TODO
# import communities
communities_2020 = gpd.read_file('data/derived/communities/communities.geojson')

# import grid capacity data (2023, is that a problem?)
capacity_2023 = pd.read_csv('data/final/data/renewable_capacity.csv')

# import grid generation data (select year 2020 data)
generation = pd.read_csv('data/final/data/renewable_generation.csv')
generation_2020 = generation.loc[generation['year'] == 2020]



# assign aggregated grid-level data (total capacity, renewable capacity ratio, annual generation)
add_capacity = pd.merge(communities_2020, capacity_2023, how='left', on='intertie_id')
add_generation = pd.merge(add_capacity, generation_2020, how='left', on='intertie_id')

aggregated = add_generation

# assign grid category: regional or remote
aggregated['en_category'] = pd.Series(dtype='string')
aggregated['en_category'] = 'Islanded'

aggregated.loc[aggregated['intertie_id'] == '215-1985', 'en_category'] = 'Regional'

# subset columns of interest
sub = aggregated[[
    'fips',
    'name',
    'intertie_id',
    'total_population',
    'en_category',
    'renewable_capacity_mw',
    'sum_capacity_mw',
    'generation_mwh',
    'geometry'
]]

# rename the subsetted columns
sub.rename(inplace=True, columns={
    'total_population': 'population',
    'renewable_capacity_mw': 'grid_renewable_capacity_mw',
    'sum_capacity_mw': 'grid_capacity_mw',
    'generation_mwh': 'grid_annual_generation_mwh'
})


# glennallen, cordova, sitka (generation), alakanuk, st. mary's


sub.explore()
