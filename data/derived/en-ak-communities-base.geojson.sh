#!/usr/bin/bash

target_file=$(basename $BASH_SOURCE .sh)

if [ -f $target_file ]; then
  echo "skipping creation: $target_file exists"
  exit 0
fi

source_file="../source/ak-dol.places2020/data/ak-dol.places2020.geojson"

if [ ! -f $source_file ]; then
  # run the get_it script .. continue if it doesn't fail
  echo "Failed to access $source_file"
  echo "go run the get_it.sh script and try again"
  exit 1
fi

# ogr2ogr with the magic sauce!

