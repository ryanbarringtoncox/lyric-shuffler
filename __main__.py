#!/usr/bin/python
import sys, random
shuffled_words=[]
words_per_line=[]
debug=True
remove_boring_words=True
filename='lyrics.txt'

# all lower case please
boring_words = ['i','you','the','is','my','it','but','in','a']

# grab each line of plain txt file
with open(filename) as f:
  content = f.readlines()
f.close

# remove unwanted charsand empty lines
for line in content:
  line=line.replace('"','').replace('\'','').replace('.','').replace(',','').strip('\n')
  if line: 
    # split into words
    curr_words = line.split()
    # add words to shuffled_words list, keep count of words/line
    counter=0
    for word in curr_words:
      counter = counter+1
      word = word.lower()
      # convert words to lower case and remove boring words if remove_boring_words=True
      if not remove_boring_words: shuffled_words.append(word)
      elif word not in boring_words: shuffled_words.append(word)
    words_per_line.append(counter)

# calculate average words per line
avg_wpl = reduce(lambda x, y: x + y, words_per_line)/len(words_per_line)

if debug:
  print "shuffled_words before they are shuffled:"
  print shuffled_words
  print "Average words per line is " + str(avg_wpl)

# shuffle word list
random.shuffle(shuffled_words)

if debug:
  print "shuffled_words after they are shuffled:"
  print shuffled_words

# print shuffled words
counter=0
for word in shuffled_words:
  counter = counter+1
  print word,
  if counter % avg_wpl == 0:
    print 
