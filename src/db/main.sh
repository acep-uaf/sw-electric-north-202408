#!/bin/bash

# if you deleted the database in order to rebuild:
#            don't forget to load spatial support!
#            CREATE EXTENSION postgis;

./src/db/ddl/create_tables.sh
./src/db/csv_to_postgres.sh
./src/db/geojson_to_postgres.sh