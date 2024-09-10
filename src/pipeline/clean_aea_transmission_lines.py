import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs

# read to memory the Alaskan transmission line shapefile
# (shapefile directory is stashed in the repo and .gitignored, circumvents Google Drive Auth meltdown)
raw = gpd.read_file('data/raw/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp')

raw.Voltage = raw.Voltage.str.replace(r'KV$', '', regex=True)   # drop 'KV' from voltages
raw.Voltage = raw.Voltage.str.replace(r'<', '', regex=True)     # drop '<' from voltages
raw.Voltage = raw.Voltage.str.split('-').str[0]                 # split on '-', keep lower value
raw.Voltage = pd.to_numeric(raw.Voltage)                        # convert string to numeric
raw.Voltage = raw.Voltage.round()                               # round off the decimals

clean = raw

clean.plot()


clean.to_file('data/derived/aea_transmission_lines.geojson', driver = 'GeoJSON')
