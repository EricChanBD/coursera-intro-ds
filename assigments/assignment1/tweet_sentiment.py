import sys
sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# sent_file = open("AFINN-111.txt")

# <codecell>

scores = {} # initialize an empty dictionary

# <codecell>

for line in sent_file:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# <headingcell level=2>

# Loads tweets from .json

# <codecell>

import json
import re

# <codecell>

# tweet_file = open('output.txt')

# <codecell>

tweets = []

# <codecell>

for line in tweet_file:
    dic = json.loads(line)
    try:
        tweets.append(dic['text'])
    except:
        pass # no real tweet

# <codecell>

for tweet in tweets:
    words = tweet.split()
    score = 0
    for word in words:
        word = re.search('[a-zA-Z]+', word)
        word = '' if word is None else word.group().lower()
        try:
           score = score + scores[word]
        except:
            pass
    print score

# <codecell>

