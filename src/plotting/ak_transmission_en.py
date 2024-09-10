import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs

crs = ccrs.NorthPolarStereo()
crs_proj4 = crs.proj4_init
polar_aea_transmission_lines = aea_transmission_lines.to_crs(crs_proj4)
polar_aea_transmission_lines.plot()

# read to memory the Electric North countries shapefile
en_outline = gpd.read_file('data/raw/Shapefile_export/EN_outline.shp')

crs = ccrs.NorthPolarStereo()
crs_proj4 = crs.proj4_init
polar_en_countries = en_outline.to_crs(crs_proj4)
polar_en_countries.plot()



ax = polar_aea_transmission_lines.plot(color = "green")
polar_en_countries.plot(ax = ax, color="lightblue")
