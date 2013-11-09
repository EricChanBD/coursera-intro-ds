import sys
sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

# Load terms

# <codecell>

# sent_file = open("AFINN-111.txt")

# <codecell>

scores = {} # initialize an empty dictionary

# <codecell>

for line in sent_file:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# Q5

# <codecell>

import json
import re

# <codecell>

tweets = []

# <codecell>

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

# <codecell>

# tweet_file = open('output.txt')

for line in tweet_file:
    dic = None
    try:
        dic = json.loads(line)
    except:
        continue
    
    # Find the state
    state = None
    
    # Look at place tag
    place = None
    try:
        place = dic['place']
    except: pass
    
    if place is not None:
        if place['country_code'] == 'US':
            state = place['full_name'][-2:].upper()
    
    if state is not None and not state in states:
        state = None
    
    # Look at user tag
    if state is None:
        try:
            state = dic['user']['location'][-2:].upper()
        except:
            continue
    if state is not None and not state in states:
        state = None
    
    # add to the list
    if state is not None:
        try:
            tweets.append((dic['text'], state))
        except:
            pass # no real tweet

# <codecell>

# print len(tweets)

# <codecell>

state_score = {}
for state in states:
    state_score[state] = 0

# <codecell>

for tweet, state in tweets:
    score = 0
    words = re.findall('[a-zA-Z]+', tweet)
    words = [word.lower().strip() for word in words]
    for word in words:
        try:
           score = score + scores[word]
        except:
            pass
    
    try:
        state_score[state] = state_score[state] + score
    except:
        continue
    # print score, tweet.encode('utf-8'), state

# <codecell>

state_score

# <codecell>

sorted_states = sorted(state_score, key=state_score.get, reverse=True)

# <codecell>

print sorted_states[0]