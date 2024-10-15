#!/bin/sh

# final 
# set path
final=./src/final
# loop and run scripts
for f in $final/en_us_ak_communities.py \
        $final/en_us_ak_powerplants.py \
        $final/en_us_ak_transmission.py
do
    python $f
done
