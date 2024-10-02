#!/bin/sh

file_path=./src/raw

for f in $file_path/*.py
do
    python $f 
done