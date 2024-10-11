#!/bin/bash

# spec out the database. Note: password is stashed in local .pgpass file, no need to call
PG="dbname=testing host=localhost port=5432 user=ian"

# Works great! Don't change!
for filename in data/raw/*.geojson; do

    tablename="$(basename "${filename%.geojson}")"

    ogr2ogr -f "PostgreSQL" \
        PG:"$PG" \
        "$filename" \
        -nln "$tablename" \
        -overwrite

    echo $filename
    echo "written as $tablename"
    
done
