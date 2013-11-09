from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: word
    # value: filename
    value = record[0]
    text = record[1]
    for key in text.split():
        mr.emit_intermediate(key, value)

def reducer(key, values):
    # key: word
    # value: list of filenames
    mr.emit((key, list(set(values))))

if __name__ == '__main__':
    import sys, json
    inputdata = open(sys.argv[1])
    # inputdata = open('./data/books.json')
    mr.execute(inputdata, mapper, reducer)

    with open('inverted_index.json', 'w') as outfile:
        json.dump(mr.result, outfile)
