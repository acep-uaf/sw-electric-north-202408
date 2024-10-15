#!/bin/sh

# raw
# set path
raw=./src/raw
# loop through python scripts and run
for f in $raw/*.py
do
    python $f 
done




