# `raw/`
The scripts in this directory (and corresponding outputs in `data/raw`) are bare minimal transformations of external data sources. Most scripts are rudimentary API calls, where a URL string is accessed and saved to file. This operation was largely done using Pandas and GeoPandas.  

A few simple custom functions were written and can be found in `raw/functions/`: 
- `api_geo.py` calls an API using GeoPandas, converts the CRS to 3338, then writes to disk. 
- `api_xlsx.py` reads an XLSX file from URL and writes to disk.

Filenames of scripts correspond to the source organization:
## `aetr.py` Alaska Energy Trends Report [homepage](https://acep-uaf.github.io/aetr-web-book-2024/)
This script pulls generation data from AETR and writes to disk.
<br>

## `cases.py` Community Appropriate Sustainable Energy Security [homepage](https://renewableenergy.usask.ca)
This script pulls shapefiles from a .gitignored copy of the Google Drive CASES folder. In the future, this data source may be more publicly available and we will rebuild this script. Files generated are as follows:
### `cases_boundary.geojson'`
Polyline of Electric North boundary. Area latitudinally above the line is said to be part of Electric North. 
### `cases_regional_grids_capacity.geojson`
Polygons containing outline of Electric North 'regional grids', or areas with real transmission lines, grids not islanded or remote. Also has attribute data for capacity of renewables/non-renewables.
### `cases_regional_grids.geojson`
Polygons containing outline of Electric North 'regional grids', or areas with real transmission lines, grids not islanded or remote.
### `cases_transmission.geojson`
Polyline of `transmission` lines within AK. Air-quoted because many transmission lines in AK are such low voltage they would be classified as distribution lines elsewhere.
<br>

## `census.py` U.S. Census Bureau [homepage](https://www.census.gov)
This script pulls U.S. Gazetteer Files from the 2024 Census for Alaska. Output file is:
### `census_2024_gaz_places.geojson`
<br>

## `dcced.py` Alaska Department of Commerce, Community, and Economic Development [homepage](https://www.commerce.alaska.gov/web/)
This script pulls AK community point data and writes to:
### `dcced_communities.geojson`
<br>

## `dnr.py` Alaska Department of Natural Resources [homepage](https://dnr.alaska.gov)
This script pulls a polyline of the coast of Alaska from AK DNR. Saved to:
### `dnr_coastline.geojson`
<br>

## `dol.py` Alaska Department of Labor [homepage](https://labor.alaska.gov)
This script pulls community polygons from AK DOL. Polygons contain attribute data for population and demographics. Output is saved to:
### `dol_places_2020.geojson`
<br>

## `en.py` Electric North [webmap](https://spatialsk.maps.arcgis.com/apps/dashboards/074e5f3d85464d7d8095035f41f53d42)
This script extracts a template/target table from an emailed geodatabase. This is the poor quality data that we are trying to replace. Output is written to file as:
### `en_population_locations.geojson`
<br>

## `es.py` Alaskan Energy Statistics [homepage](https://acep-uaf.github.io/ak-energy-statistics-2011_2021/)
This script pulls two XLSX workbooks from GitHub, extracts a few sheets, and writes them to file. Outputs are:
### `es_annual_operations.csv`
PCE operations data, 2001-2021
### `es_gen_fuel_type.csv`
PCE generation data by fuel type, 2001-2021
### `es_infrastructure.csv`
PCE installed infrastructure data (generators), 2021
### `es_lookup_interties.csv`
PCE interties and associated communities
### `es_lookup_plants.geojson`
PCE powerplants as a spatial file with intertie data
### `es_lookup_sales_report.geojson`
PCE sales reporting data as a spatial file
### `es_monthly_gen.csv`
PCE generation data by month, 2001-2021
<br>

## `usgs.py` U.S. Geological Survey [homepage](https://www.usgs.gov)
This script pulls data from a USGS rest server and writes to file. Outputs are:
### `usgs_incorporated.geojson`
Spatial file of incorporated communities in Alaska
### `usgs_places.gesojson`
Spatial file of places in Alaska (some communities, some place of interest)
### `usgs_unincorporated.gesojson`
Spatial file of unincorporated communities in Alaska
<br>

