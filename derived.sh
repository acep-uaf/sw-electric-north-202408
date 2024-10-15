#!/bin/sh

# derived
# set path
derived=./src/derived
# loop and run scripts without dependencies in derived
for f in $derived/infrastructure.py \
        $derived/interties.py \
        $derived/lookup_fips_interties.py \
        $derived/transmission.py
do
    python $f
done
# loop and run scripts with dependencies in derived
for f in $derived/community_polygons.py \
        $derived/community_points.py \
        $derived/plants.py \
        $derived/lookup_plant_name_id.py \
        $derived/generation.py \
        $derived/renewable_generation.py \
        $derived/renewable_capacity.py
do
    python $f
done
