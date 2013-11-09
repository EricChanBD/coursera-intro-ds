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

new_terms = {}

# <codecell>

for tweet in tweets:
    score = 0
    words = re.findall('[a-zA-Z]+', tweet)
    words = [word.lower().strip() for word in words]
    for word in words:
        try:
           score = score + scores[word]
        except:
            # if word is not on loaded terms
            try:
                new_terms[word]
                # word already on new_terms
            except:
                # word is not on new_terms
                new_terms[word] = []
    #print score, tweet
    
    for word in words:
        try:
            new_terms[word].append(score)
        except:
            pass
            # word is on scores (not new term) so is not needed

# <codecell>

for key in new_terms.iterkeys():
    scores = new_terms[key]
    print key, reduce(lambda x, y: x + y, scores) / len(scores)

# <codecell>


