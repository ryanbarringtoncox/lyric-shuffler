#!/bin/bash
curr_dir=`pwd`
target_path="$curr_dir/run.py"
link_path="/usr/local/bin/lyric-shuffler"

if [ -L $link_path  ]; then
  echo "lyric-shuffler is already in your path"
  echo "  ...exiting"
  exit
fi

echo "Sym-linking..."
echo "sudo ln -s $target_path $link_path"
sudo ln -s $target_path $link_path
echo "  ...done"
echo "Usage: lyric-shuffler some-lyrics.txt some-more-lyrics.txt you-get-the-idea.txt"
