from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: 
    # value: 
    L = 5
    N = 5
    which = record[0].encode('utf-8')
    value = record[3]
    if which == 'a':
        for k in range(N):
            i = record[1]
            j = record[2]
            key = (i,k)
            mr.emit_intermediate(key, (j, value))
    if which == 'b':
        for i in range(L):
            j = record[1]
            k = record[2]
            key = (i,k)
            mr.emit_intermediate(key, (j, value))

def reducer(key, values):
    # key: 
    # value: 
    N = 5
    s = 0

    for j in range(5):
        filter_values = [value for value in values if value[0] == j]
        if len(filter_values) < 2:
            pass
        if len(filter_values) == 2:
            s = s + filter_values[0][1] * filter_values[1][1]
    mr.emit((key[0], key[1], s))

if __name__ == '__main__':
    import sys, json
    inputdata = open(sys.argv[1])
    # inputdata = open('./data/matrix.json')
    mr.execute(inputdata, mapper, reducer)

    with open('multiply.json', 'w') as outfile:
        json.dump(mr.result, outfile)




