from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: tuple of the friendship
    # value: count
    key = tuple(sorted((record[0], record[1])))
    value = 1
    mr.emit_intermediate(key, value)

def reducer(key, values):
    # key: tuple of the friendship
    # value: 1 if is friend
    if len(values) == 1:
        mr.emit((key[0], key[1]))
        mr.emit((key[1], key[0]))

if __name__ == '__main__':
    import sys, json
    inputdata = open(sys.argv[1])
    # inputdata = open('./data/friends.json')
    mr.execute(inputdata, mapper, reducer)

    with open('asymmetric_friendships.json', 'w') as outfile:
        json.dump(mr.result, outfile)
