from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: order_id
    # value: record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, values):
    # key: order_id
    # value: records
    for value in values[1:]:
        mr.emit(values[0] + value)

if __name__ == '__main__':
    import sys, json
    inputdata = open(sys.argv[1])
    # inputdata = open('./data/records.json')
    mr.execute(inputdata, mapper, reducer)

    with open('join.json', 'w') as outfile:
        json.dump(mr.result, outfile)
