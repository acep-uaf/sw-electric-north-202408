# `src/`

<br>

## `main.sh`
Although not located in `src/`, it's worth talking about here for context. Running `./main.sh` from the root directory will run the pipeline start to finish, executing all scripts in `src/` and overwriting all data in `data/`. 

Pipeline scripts are devided into three different folders, `raw/`, `derived/`, and `final/`, which correspond to increasing levels of cleanliness and organization. 

<br>

## `raw/`
The scripts in this directory (and corresponding outputs in `data/raw`) are bare minimal transformations of external data sources. Most scripts are rudimentary API calls, where a URL string is accessed and saved to file. This operation was largely done using Pandas and GeoPandas.  

A few simple custom functions were written and can be found in `raw/functions/`: 
- `api_geo.py` calls an API using GeoPandas, converts the CRS to 3338, then writes to disk. 
- `api_xlsx.py` reads an XLSX file from URL and writes to disk.

Filenames of scripts correspond to the source organization:
- `aetr.py` = Alaska Energy Trends Report
- `cares.py` = 