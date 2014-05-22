#!/bin/bash
all_lyrics_file="all_lyrics.txt"

# holds unshuffle lyrics
if [ -f $all_lyrics_file ]; then
  rm $all_lyrics_file
fi
touch $all_lyrics_file

# validate songs dir
if [ ! -d $1 ]; then
  echo $1 is not a valid dir
  exit
fi

# loop through *.txt files in songs dir and cat to all_lyrics file
for f in $1/*.txt
do
  cat $f >> $all_lyrics_file
  echo "" >> $all_lyrics_file 
done

# shuffle up all_lyrics to stdout
./word-shuffler.py $all_lyrics_file 
