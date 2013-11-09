from __future__ import division


import sys
tweet_file = open(sys.argv[1])

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

frequency = {}

# <codecell>

for tweet in tweets:
    words = re.findall('[a-zA-Z]+', tweet)
    words = [word.lower().strip() for word in words]
    for word in set(words):
        try:
            frequency[word] = frequency[word] + 1
        except:
            frequency[word] = 1

# <codecell>

total_occurrences = reduce(lambda x, y: x + y, frequency.values())

# <codecell>

# from __future__ import division

# <codecell>

for key in frequency.iterkeys():
    print key, frequency[key] / total_occurrences

# <codecell>
