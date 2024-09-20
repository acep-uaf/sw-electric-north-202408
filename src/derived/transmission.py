import geopandas as gpd

# clean up string voltage, convert to numeric, cut to 100 KV
def voltage_cleaning(input, output, voltage_limit):
    raw = gpd.read_file(input)
    raw.Voltage = (raw.Voltage.str.replace(r'[<KV-]', '', regex=True)
                        .str.split('-').str[0]
                        .astype(float).round())
    clean = raw[raw['Voltage'] >= voltage_limit]
    clean_3338 = clean.to_crs(3338)
    clean_3338.to_file(output)

voltage_cleaning(
    input = 'data/source/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp',
    output = 'data/derived/transmission.geojson',
    voltage_limit = 0)

# test = gpd.read_file('data/raw/en_regional_grids_capacity.geojson')
# test.explore()