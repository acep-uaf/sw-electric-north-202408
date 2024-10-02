import geopandas as gpd
import pandas as pd

# load polygons with population data
# load points with intertie data
polys = gpd.read_file('data/raw/dol_places_2020.geojson')
points = gpd.read_file('data/raw/es_lookup_sales_report.geojson')


# cleaning
polys.rename(inplace=True, columns={
    'NAME':'name',
    'STATE':'state',
    'PLACE':'place',
    'FIPS':'fips',
    'TOTALPOP':'total_population',
    'WHITE':'white',
    'BLACK':'black',
    'NATIVE':'native',
    'ASIAN':'asian',
    'PACISLAND':'pacific_islander',
    'OTHER':'other',
    'TWO_PLUS':'two_plus',
    'HISPANIC':'hispanic',
    'NATALNCOMB':'native_indian_combo',
    'GRPQTRS':'group_quarters',
    'HOUSEUNITS':'housing_units',
    'VACANT':'vacant_housing_units',
    'OCCUPIED':'occupied_housing_units'})


# drop 'CDP', 'city', 'municipality', 'city and borough'
polys['name'] = polys['name'].str.replace(r'\b(CDP|city|and|borough|municipality)\b', '', regex=True).str.strip()


polys.sort_values(by='name', inplace=True)


# clean intertie data 
points.rename(inplace=True, columns={
    'Sales Reporting ID':'sales_reporting_id',
    'OPERATOR_AEA Operator ID':'aea_operator_id',
    'EIA operator Number':'eia_operator_number',
    'PCE Reporting ID':'pce_reporting_id',
    'EIA Sales reporting frequency':'eia_reporting_frequency',
    'PCE Sales reporting frequency':'pce_reporting_frequency',
    'Reporting Name':'reporting_name',
    'OPERATOR_Operator Name':'operator_name',
    'RCA CPCN':'rca_cpcn',
    'INTERTIE_Current Intertie ID':'intertie_id',
    'INTERTIE_Current Intertie name':'intertie_name',
    'Index Community':'name',
    'GNIS':'gnis',
    'Latitude':'latitude',
    'Longitude':'longitude',
    'AEA energy region':'aea_energy_region',
    'Communities reported':'communities_reported'
})

p = points[[
    'intertie_id',
    'intertie_name',
    'name'
]]

# select a few rows to make the basic lookup table
l = polys[[
    'name',
    'state',
    'place',
    'fips'
    ]]

# # make new column intertie_id, set as null
# l['intertie_id'] = 'NA'
# l['intertie_name'] = 'NA'

merged = l.merge(p, on='name', how='left')
# merged.drop_duplicates(subset=['fips'], inplace=True)
m = merged.dropna()

merged_dict = dict(zip(m['fips'], m['intertie_id']))

# manual assignment of non-matching
railbelt_id = '215-1985'
# make a dictionary of fips codes to intertie_id
manual_dict = {
    '0201305': '005-0000', # Alatna
    '0201420': '169-0000', # Aleknagik
    '0203110': railbelt_id, # Anchor Point
    '0203220': railbelt_id, # Anderson
    '0205000': railbelt_id, # Badger
    '0205585': railbelt_id, # Bear Creek
    '0206245': railbelt_id, # Beluga
    '0206850': railbelt_id, # Big Delta
    '0207070': railbelt_id, # Big Lake
    '0209657': railbelt_id, # Buffalo Soapstone
    '0209710': railbelt_id, # Butte
    '0210150': railbelt_id, # Cantwell
    '0212350': railbelt_id, # Chase
    '0212920': railbelt_id, # Chena Ridge
    '0212970': '101-0000', # Chenega (Bay)
    '0213860': '223-0000', # Chiniak
    '0215320': railbelt_id, # Clam Gulch
    '0216420': railbelt_id, # Cohoe
    '0216750': railbelt_id, # College
    '0217190': railbelt_id, # Copper Landing
    '0217300': '216-0000', # Copper Center (Copper Valley Electric Assoc)
    '0217670': '032-1998', # Covenant Life
    '0217960': railbelt_id, # Crown Point
    '0218620': railbelt_id, # Delta Junction
    '0218675': railbelt_id, # Deltana
    '0218805': railbelt_id, # Denali Park
    '0218925': railbelt_id, # Diamond Ridge (Homer)
    '0219750': '015-2008', # Dot Lake Village
    '0220600': '009-0000', # Eagle Village
    '0223460': railbelt_id, # Ester
    '0223790': '007-0000', # Evansville
    '0225000': railbelt_id, # Farm Loop (Palmer)
    '0224980': railbelt_id, # Farmers Loop (Fairbanks)
    '0225220': railbelt_id, # Ferry
    '0225550': railbelt_id, # Fishhook
    '0226100': railbelt_id, # Fort Greely
    '0226835': railbelt_id, # Four Mile Road (Nenana)
    '0226870': railbelt_id, # Fox
    '0226910': railbelt_id, # Fox River (Homer)
    '0227090': railbelt_id, # Fritz Creek (Homer)
    '0227145': railbelt_id, # Funny River
    '0228200': railbelt_id, # Gateway
    '0228740': '216-0000', # Glenallen (Copper Valley Electric Assoc)
    '0229130': railbelt_id, # Goldstream
    '0230500': '216-0000', # Gulkana (Copper Valley Electric Assoc)
    '0231270': railbelt_id, # Halibut Cove
    '0231710': railbelt_id, # Happy Valley
    '0231765': railbelt_id, # Harding-Birch Lakes
    '0232150': railbelt_id, # Healy
    '0233580': railbelt_id, # Hope
    '0233800': railbelt_id, # Houston
    '0236540': railbelt_id, # Kachemak (Homer)
    '0237250': railbelt_id, # Kalifornsky
    '0237650': '023-2015', # Kasaan
    '0238090': railbelt_id, # Kasilof
    '0238420': railbelt_id, # Kenai
    '0238910': '216-0000', # Kenny Lake (Copper Valley Electric Assoc)
    '0239630': '150-0000', # King Salmon
    '0240670': railbelt_id, # Knik River
    '0240645': railbelt_id, # Knik-Fairview
    '0241210': '223-0000', # Kodiak Station 
    '0242160': '217-2009', # Kupreanof (Petersburg)
    '0243260': railbelt_id, # Lazy Mountain
    '0245295': railbelt_id, # Lowell Point (Seward)
    '0245700': '032-1998', # Lutak (Haines)
    '0247735': railbelt_id, # Meadow Lakes
    '0248590': '196-0000', # Mertarvik (Newtok relocation)
    '0249200': '223-0000', # Mill Bay (Kodiak)
    '0250080': railbelt_id, # Mooose Creek
    '0250190': railbelt_id, # Moose Pass
    '0250800': '032-1998', # Mosquito Lake (Haines)
    '0251455': '032-1998', # Mud Bay (Haines)
    '0253050': railbelt_id, # Nenana
    '0253270': '123-1983', # Newhalen
    '0254050': railbelt_id, # Nikiski
    '0254085': railbelt_id, # Nikolaevsk
    '0254480': railbelt_id, # Ninilchik
    '0255030': '123-1983', # Nondalton
    '0255745': railbelt_id, # North Lakes
    '0255910': railbelt_id, # North Pole
    '0258330': '034-1988', # Oscarville (Bethel)
    '0258660': railbelt_id, # Palmer
    '0261120': railbelt_id, # Pleasant Valley
    '0261788': railbelt_id, # Point MacKenzie
    '0263610': '223-0000', # Port Lions
    '0264240': railbelt_id, # Primrose
    '0265345': railbelt_id, # Ridgeway
    '0266510': railbelt_id, # Salamatof
    '0266550': railbelt_id, # Salcha
    '0267570': '217-2009', # Saxman
    '0268340': railbelt_id, # Seldovia
    '0268370': railbelt_id, # Seldovia Village
    '0270320': '216-0000', # Silver Springs
    '0271640': railbelt_id, # Soldotna
    '0272135': railbelt_id, # South Lakes
    '0272190': '150-0000', # South Naknek
    '0272230': railbelt_id, # South Van Horn
    '0266140': '075-1985', # St. Mary's
    '0266360': '084-2015', # St. Michael
    '0266470': '180-0000', # St. Paul
    '0272985': railbelt_id, # Steele Creek
    '0273070': railbelt_id, # Sterling
    '0274350': railbelt_id, # Susitna North
    '0274525': railbelt_id, # Sutton-Alpine
    '0274830': railbelt_id, # Talkeetna
    '0275050': '015-2008', # Tanacross
    '0275077': railbelt_id, # Tanaina
    '0275480': '216-0000', # Tazlina
    '0277140': '023-2015', # Thorne Bay
    '0278680': railbelt_id, # Trapper Creek
    '0279830': railbelt_id, # Two Rivers
    '0279890': railbelt_id, # Tyonek
    '0281320': '052-2005', # Upper Kalskag
    '0284510': railbelt_id, # Whittier
    '0285280': railbelt_id, # Willow
    '0285290': '216-0000', # Willow Creek (Copper Valley Electric Assoc)
    '0285680': '223-0000' # Womens Bay
}

lookup_dict = {**merged_dict, **manual_dict}

merged['intertie_id'] = merged['fips'].map(lookup_dict)
merged.drop_duplicates(subset=['fips'], inplace=True)


lookup = merged[['fips', 'intertie_id']]


lookup.to_csv('data/derived/lookup_fips_interties.csv', index=False)


# load = pd.read_csv('data/derived/lookup_interties_fips/data/lookup_fips_interties.csv')

















