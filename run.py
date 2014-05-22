#!/bin/bash

if [ ! -d $1 ]; then
  echo $1 is not a valid dir
  exit
fi

for f in $1/*.txt
do
  #echo found $f
  ./word-shuffler.py $f
done
