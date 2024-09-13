#!/usr/bin/bash

function purge() {
  # toast the zip file
  # toast the folder 
  echo "purge!"
}


if [ ! -f Places2020.zip ]; then
  echo "downloading the Places2020.zip"
  wget `cat Places2020.zip.url`
  if [ $? -eq 0 ]; then
    echo "download successful!"
  else
    echo "Error: unable to wget Places2020.zip"
    exit 1
  fi
else
  echo "File exists Places 2020.zip: skipping downloading"
fi

# todo - check sha sum - purge & error on failed sha check

if [ ! -d extract ]; then
  echo "extracting Places2020.zip to extract"
  unzip Places2020.zip -d extract
else
  echo "extract already completed. skipping unzip"
fi

CMD="ogr2ogr -f GeoJSON ak-dol.places2020.geojson extract/Places2020.shp -t_srs EPSG:3338"
if [ ! -f ak-dol.places2020.geojson ]; then
  echo "creating the ak-dol.places2020 with ogr2ogr"
  $CMD
  if [ $? -eq 0 ]; then
    echo "conversion successful"
  else
    echo "Failed: $CMD"
    echo "Fix this!!"
    exit 1
  fi
fi

echo "Wow! We have ak-dol.places2020.geojson as an EPSG:3338 file"
