from __future__ import division

import sys
tweet_file = open(sys.argv[1])


# Q6

# <codecell>

import json

# <codecell>

# tweet_file = open('output.txt')

# <codecell>

hashtags_count = {}

# <codecell>

for line in tweet_file:
    dic = json.loads(line)
    try:
        hashtags = dic['entities']['hashtags']

        for hashtag in hashtags:
            hashtag = hashtag['text'].lower()
            try:
                hashtags_count[hashtag] = hashtags_count[hashtag] + 1
            except:
                hashtags_count[hashtag] = 1
    except:
        pass # no real tweet or no hashtags

# <codecell>

sorted_tags = sorted(hashtags_count, key=hashtags_count.get, reverse=True)

# <codecell>

for tag in sorted_tags[:10]:
    print tag, hashtags_count[tag]

# <codecell>
