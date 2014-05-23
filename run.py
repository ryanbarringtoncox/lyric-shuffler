#!/bin/bash

# temp file to hold concatted, unshuffled lyrics
all_lyrics_file="all_lyrics.tmp"

if [ $# -eq 0 ]; then
  echo "No args supplied"
  echo "Usage: lyric-shuffler some-lyrics.txt some-more-lyrics.txt you-get-the-idea.txt"
  exit
fi

# if file exists, remove and start afresh
if [ -f $all_lyrics_file ]; then
  rm $all_lyrics_file
fi
touch $all_lyrics_file

# loop through txt files and cat to all_lyrics.tmp file
for f in "$@"
do
  cat $f >> $all_lyrics_file
  echo "" >> $all_lyrics_file 
done

# shuffle all_lyrics, print to stdout
./word-shuffler.py $all_lyrics_file 
