#!/bin/sh

# source
# set path
raw=./src/source
# loop through python scripts and run
for f in $raw/*.py
do
    python $f 
done
