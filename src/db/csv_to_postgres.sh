#!/bin/bash

# # example syntax
# "\copy source-table from 'source-table.csv' with DELIMITER ','"
# "\copy $tablename from '$filename' with DELIMITER ',' CSV HEADER"

# loop, add data to empty tables
for filename in data/raw/*.csv; do

    tablename="$(basename "${filename%.csv}")"

    echo "\copy $tablename from '$filename' with DELIMITER ',' CSV HEADER" | psql -h localhost -U ian -d testing
    echo $tablename
    echo $filename

done