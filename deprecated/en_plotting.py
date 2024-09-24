import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs

import matplotlib.pyplot as plt

# set up polar projection
crs = ccrs.NorthPolarStereo(central_longitude=-150)
crs_proj4 = crs.proj4_init

# read alaska coastline file, convert to polar-centric
raw_alaska_coastline = gpd.read_file('data/raw/alaska_coastline.geojson')
alaska_coastline = raw_alaska_coastline.cx[: 0, :].to_crs(crs_proj4)  # function cx slices using a bounding box

# read Alaska Energy Authority transmission line file, convert to polar-centric projection (doesn't do much here, small area)
aea_transmission_lines = gpd.read_file('data/derived/aea_transmission_lines.geojson')
polar_aea_transmission_lines = aea_transmission_lines.to_crs(crs_proj4)




# read to memory the Electric North countries shapefile, convert to polar-centric projection
en_outline = gpd.read_file('data/raw/Shapefile_export/EN_outline.shp')
polar_en_countries = en_outline.to_crs(crs_proj4)




ax = polar_aea_transmission_lines.plot(column = 'Voltage')
alaska_coastline.plot(ax = ax, color = 'tan')
ax.axis('off')
plt.show()


# Create a figure and axis object
fig, ax = plt.subplots()
ax.axis('off')
polar_en_countries.plot(ax=ax, column=None, color="lightblue")
alaska_coastline.plot(ax=ax, color='tan')
polar_aea_transmission_lines.plot(ax=ax, column='Voltage')



# Display the plot
plt.show()
