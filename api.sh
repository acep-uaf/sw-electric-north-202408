#!/usr/bin/env bash

YAML='api.yaml'

for source in $(yq e '.source[]' "$YAML"); do
    url=$(echo "$source" | yq e '.url')
    echo "URL: $url"
done


# # todo write this as a loop
# wget -O /data/raw/dnr_coastline.geojson 'https://arcgis.dnr.alaska.gov/arcgis/rest/services/OpenData/Physical_AlaskaCoast/MapServer/1/query?outFields=*&where=1%3D1&f=geojson'
