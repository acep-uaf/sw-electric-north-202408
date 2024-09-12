# Overview
This directory contains source data, data which is manually added to the repository and from which other data files are derived. Ideally, this directory would be empty and all data sources would be derived from APIs etc. But sometimes a file is emailed and we need to use it as a stopgap until we have a more permanent source. Those files go here.

## `Alaska_population_locations.gdp.zip`
### Description:
This is a geodatabase emailed to us from University of Saskatchewan researchers. The data represents current Alaskan data used in the [Electric North map](https://spatialsk.maps.arcgis.com/apps/dashboards/074e5f3d85464d7d8095035f41f53d42). This data is known to have quality issues. It is our job to replace this data with something better. 

### Derivations:
The geodatabase is saved unchanged as `raw/alaska_population_locations.geojson`

### Notes:
This file is zipped. It's natural to want to unzip it and look inside, but you'll be disappointed. Instead, load it using GeoPandas `gpd.read_file()` function. This will read the zipped database into memory just fine. 


## `Shapefile_export/`
### Description:
This directory contains shapefiles from the `Alaska CASES` shared google drive. It's likely you don't have access and the data provenance is unknown, so for now the directory is stashed here and .gitignored. Shapefiles were extracted and saved, you're not missing out on anything. 

### Derivations:
Shapefiles were extracted and saved to `data/raw` unchanged (except `transmission.geojson`). Filenames were changed to lowercase with underscore seperators.
- `data/raw/en_outline.geojson` (An outline of the Electric North boundary)
- `data/raw/en_regional_grids.geojson` (Electric North regional grids)
- `data/raw/en_regional_grids_capacity.geojson` (Electric North regional grid capacities)
- `data/derived/transmission.geojson` (AK power lines, 100 KV and up = transmission)