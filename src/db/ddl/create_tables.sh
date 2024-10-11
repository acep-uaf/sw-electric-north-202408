#!/bin/bash

# loop through DDL directory, populate postgres with empty tables
for filename in src/db/ddl/*.sql; do

  echo "\i $filename" | psql -h localhost -U ian -d testing

done