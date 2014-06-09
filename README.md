# Lyric Shuffler                                                                                                                                                                                
## Intro

Experiment with your songwriting approach.  Draw inspiration from a scramble.  This script allows you to mash up existing song lyrics and see new word combinations.  It takes one or more plain text files (of song lyrics) and shuffles all the containing words, giving you a rich random collage.  How else will you get strange lines like "missing ripped black glass entertainment hips", "seat baby moonbeams" or "nothing to sucker for?"

## Usage

Clone the repo and cd in.  Run the install script to get lyric-shuffler in your path -

    git clone https://github.com/ryanbarringtoncox/lyric-shuffler/
    cd lyric-shuffler/
    ./install.sh

Then pass the program some plain text files full of rich words - 

    lyric-shuffler some-bitchin-lyrics.txt some-more-lyrics.txt you-get-the-idea.txt

You'll see the new output stream by on the console.  You can run it again with the same text files and the output will differ.  Write to a new file like this -

    lyric-shuffler some-lyrics.txt some-more-lyrics.txt you-get-the-idea.txt > new_file.txt

You can shuffle a whole dir like this (not recursive) -

    lyric-shuffler *

## Use with Lyric-Scraper

Built to work in conjunction with [lyric-scraper](https://github.com/ryanbarringtoncox/lyric-scraper).  Once you have both installed, you can rapidly scrape lyrics and shuffle them up.  Here's an example of scraping and shuffling Morrissey with Bob Dylan -

    lyric-scraper http://www.songlyrics.com/morrissey/ouija-board-lyrics/ 
    lyric-scraper http://www.songlyrics.com/bob-dylan/buckets-of-rain-lyrics/
    lyric-shuffler ouija-board-lyrics.txt  buckets-of-rain-lyrics.txt
