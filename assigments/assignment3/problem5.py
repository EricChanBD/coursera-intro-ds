from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: trimed string
    # value: Nothing
    key = record[1][:-10]
    value = None
    mr.emit_intermediate(key, value)

def reducer(key, values):
    # key: tuple of the friendship
    # value: Nothing
    mr.emit(key)

if __name__ == '__main__':
    import sys, json
    inputdata = open(sys.argv[1])
    # inputdata = open('./data/dna.json')
    mr.execute(inputdata, mapper, reducer)

    with open('unique_trims.json', 'w') as outfile:
        json.dump(mr.result, outfile)
