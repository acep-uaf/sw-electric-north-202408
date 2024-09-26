import geopandas as gpd

# clean up string voltage, convert to numeric, cut to 100 KV
def transmission_cleaning(input, output, voltage_limit):
    raw = gpd.read_file(input)

    raw.rename(inplace=True, columns={
        'OBJECTID':'object_id',
        'Name':'name',
        'Voltage':'voltage',
        'Source':'source',
        'Type':'type',
        'SHAPE_Leng':'shape_length',
        'Shape__Len':'shape_length2'
    })

    raw.drop(inplace=True, columns={
        'object_id',
        'shape_length',
        'shape_length2'
    })

    raw.voltage = (raw.voltage.str.replace(r'[<KV-]', '', regex=True)
                        .str.split('-').str[0]
                        .astype(float).round())
    clean = raw[raw['voltage'] >= voltage_limit]
    clean_3338 = clean.to_crs(3338)
    clean_3338.to_file(output)

transmission_cleaning(
    input = 'data/source/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp',
    output = 'data/derived/transmission/transmission.geojson',
    voltage_limit = 70)

# load = gpd.read_file('data/raw/en_regional_grids_capacity.geojson')
# load.explore()