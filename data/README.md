# `data/`
This directory contains data generated from scripts in `src`. The folders `data/raw`, `data/derived`, and `data/final` correspond to `src/raw`, `src/derived`, and `src/final`. The pipeline can be run 

## `source/`
The data in `source/` is truly source data and should be treated as if it's an external source. The directory contains data emailed or shared via Google Drive. This directory will not re-render when the pipeline is run! 
- By and large, `source/` should be left alone. 
- More information about contents can be found in `source/README.md`.

## `raw/`
The data in `raw/` has minimal cleaning. In many cases, it was pulled from a URL with a basic API, then written to disk. Contents of this directory are re-rendered when the pipeline is run via `main.sh`.
- Files here are likely of minimal use, look towards `derived/` instead.

## `derived/`
The data in `derived/` has undergone some level of transformation that distinguishes it from raw and source data. Often there has been extensive cleaning or joining of multiple data sources. Some tables are aggregated from other tables in `derived/`. Contents of this directory are re-rendered when the pipeline is run via `main.sh`.
- This directory contains data with the highest potential for use elsewhere.

## `final/`
The data in `final` is largely project-specific to the Stoatworks Electric North effort and may be of limited use to other projects. Contents of this directory are re-rendered when the pipeline is run via `main.sh`.
- If you are here from another project, check out `derived/` first.

## `db/`
This directory exists for testing purposes. Files inside are databases, so .gitignored. If you're motivated, the databases can be rendered via scripts in `src/db/`. At some point, we would like to rebuild the pipeline using SQL and DBT. This is a sandbox towards that effort.