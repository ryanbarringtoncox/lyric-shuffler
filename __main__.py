#!/usr/bin/python
import sys, random
scrambled_words=[]
words_per_line=[]
debug=False
filename='lyrics.txt'

# grab each line of plain txt file
with open(filename) as f:
  content = f.readlines()
f.close

# remove double quotes and empty lines
for line in content:
  line=line.replace('"','').strip('\n')
  if line: 
    # split into words
    curr_words = line.split()
    # scramble words, add to list, keep count or words/line
    counter=0
    for word in curr_words:
      counter = counter+1
      scrambled_words.append(word)
    words_per_line.append(counter)

# calculate average words per line
avg_wpl = reduce(lambda x, y: x + y, words_per_line)/len(words_per_line)
if debug:
  print "scrambled_words before they are scrambled:"
  print scrambled_words
  print "Average words per line is " + str(avg_wpl)

# shuffle word list
random.shuffle(scrambled_words)

if debug:
  print "scrambled_words after they are scrambled:"
  print scrambled_words

# print shuffled words
counter=0
for word in scrambled_words:
  counter = counter+1
  print word,
  if counter % avg_wpl == 0:
    print 
