from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, values):
    # key: person
    # value: friend
    mr.emit((key, len(values)))

if __name__ == '__main__':
    import sys, json
    # inputdata = open(sys.argv[1])
    inputdata = open('./data/friends.json')
    mr.execute(inputdata, mapper, reducer)

    with open('asymmetric_friendships.json', 'w') as outfile:
        json.dump(mr.result, outfile)
