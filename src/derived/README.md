# `derived/`
The scripts in this directory (and corresponding outputs in `data/derived/`) represent the bulk of the processing in the pipeline. The outputted tables have undergone cleaning and transformations, and thus source prefixes are dropped from the filenames. 

It's worth noting that there's much more complexity in this phase than in `raw/` or `final/`. The complexity of scripts and dependencies is enough to consider tooling such as `dbt` or `dagster`. It's pretty difficult to keep things straight and run the scripts in order as is. Thoughts of scaling upwards without additional tooling seem foolish. 

Not to mention data validation, unit testing, or script dependency diagrams. If only...
<br>

## `community_points.py`
Inputs:
- `raw/census_2024_gaz_places.geojson`
- `derived/communities.geojson`
- `derived/lookup_fips_interties.csv`

Outputs:
- `community_points.geojson`

This script extracts id and point geometry from census, drops polygon geometry from communities, and replaces with point geometry (joining on FIPS id).
<br>


## `community_polygons.py`
Inputs:
- `raw/dol_places_2020.geojson`
- `derived/lookup_fips_interties.csv`

Outputs:
- `community_polygons.geojson`

This script ingests polygons (with population and demographic attributes) and joins a lookup table using the FIPS id. This allows polygons to be associated with `intertie_id`, a powerful foreign key.
<br>


## `generation.py`
Inputs:
- `raw/aetr_generation.csv`
- `derived/lookup_plant_name_id.csv`

Outputs:
- `generation.csv`

This script loads generation data from AETR and joins a lookup table in order to assign plant id to plant names. 
<br>


## `infrastructure.py`
Inputs:
- `raw/es_infrastructure.csv`

Outputs:
- `infrastructure.csv`

This script ingests Energy Stats infrastructure data, renames columns, subsets columns, then writes to file.
<br>


## `interties.py`
Inputs:
- `raw/es_lookup_interties.csv`

Outputs:
- `interties.csv`

This script loads intertie data from Energy Stats, renames columns, cleans string data for intertie name, subsets columns, then writes to file. 
<br>


## `lookup_fips_interties.py`
Inputs:
- `raw/dol_places_2020.geojson`
- `raw/es_lookup_sales_report.geojson`

Outputs:
- `lookup_fips_interties.csv`

This script is a monster. And it's absolutely pivitol to making this pipeline work. Upstream, we have state and federal data that we would very much like to join to data sourced from Energy Stats and AETR. But we have no joining keys. We really want community FIPS id matched to the intertie_id used in Energy Stats. 

To do so, this code first attempts to join these two camps using matching community string names. Matches got an intertie_id. Communities that didn't match (no Railbelt communities in ES workbooks, so mostly Railbelt) were then manually assigned an intertie_id based on Energy Stats workbooks. The string-matched data was then combined with the manually-matched data and the combined dataframe written to file.
<br>

## `lookup_plant_name_id.py`
Inputs:
- `derived/plants.geojson`
- `raw/aetr_generation.csv`

Outputs:
- `lookup_plant_name_id.csv`

This script is another brute force bridge between two worlds. In this case, the object is plants and missing ID's. As above, a join on name string was run, and the unmatched plants manually-assigned an `aea_plant_id`. The combined dataframe was written to file. 
<br>


## `plants.py`
Inputs:
- `raw/es_lookup_plants.geojson`
- `derived/infrastructure.csv`

Outputs:
- `plants.geojson`

This script ingests infrastructure data, cleans column names, then adds spatial points from Energy Stats.
<br>


## `regional_grids.r`
Inputs:
- `derived/coastline.geojson`
- `derived/transmission.geojson`

Outputs:
- `regional_grids.geojson`

This script exists outside of the pipeline and is currently not used. However, there was strong interest in drawing/redrawing polygons around regional grids in Alaska. This script is a quick pass at doing so. More to come later.
<br>


## `renewable_capacity.py`
Inputs:
- `derived/infrastructure.csv`

Outputs:
- `renewable_capacity.csv`

This script is an aggregation of capacity by source by intertie. The ratio of renewable capacity was calculated. The dataframe was written to file.
<br>


## `renewable_generation.py`
Inputs:
- `derived/generation.csv`
- `derived/plants.geojson`

Outputs:
- `renewable_generation.csv`

This script is an aggregation of generation by source by intertie. The ratio of renewable generation was calculated. The dataframe was written to file. 
<br>

## `transmission.py`
Inputs:
- `data/source/Shapefile_export/AEA-Transmission_Lines-202200706/Alaska_Energy_Authority_Library.shp`

Outputs:
- `transmission.geojson`
- `transmission_all_lines.geojson`

This script ingests source data from the CASES drive (.gitignored in the repo), renames some columns, drops some columns, wrangles some horrible strings in order to extract a numeric voltage, then filters by inputted voltage. Two files were written, `transmission.geojson`, which drops all transmission lines below 70 kV, and `transmission_all_lines.geojson`, which keeps all lines regardless of voltage.
<br>