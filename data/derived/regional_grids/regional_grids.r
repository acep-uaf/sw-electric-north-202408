library(sf)
library(dplyr)
library(ggplot2)

# load coastline, transmission vector
coastline <- st_read('data/derived/coastline/coastline.geojson')
transmission <- st_read('data/derived/transmission/transmission.geojson')

# function to make a hexagonal grid with a cell size specced in meters
hex = function(x, cell_km) {
  st_make_grid(x=x, cellsize=cell_km*1000, what='polygons', square=FALSE) %>%
  st_as_sf() %>%
  st_set_crs(3338)
}

# draw hex grid of ak coast
grid = hex(coastline, 40)

# plot the hex grid over the coastline
# ggplot() +
#   geom_sf(data = coastline, fill = 'tan', color = 'black') +
#   geom_sf(data = grid, fill = NA, color = 'black') +
#   geom_sf(data = transmission, color = 'red') +
#   theme_void()


# pull grid cells that have transmission lines
grid_select <- grid[st_intersection(st_buffer(transmission, dist=20000), grid), ]

# plot it all
ggplot() +
  geom_sf(data = coastline, fill = 'tan', color = 'black') +
  geom_sf(data = grid_select, fill = 'forestgreen', color = 'black') +
  geom_sf(data = transmission, color = 'red') +
  theme_void()




st_write(grid_select, 'data/derived/regional_grids/regional_grids.geojson', delete_dsn=T)



