#!/usr/bin/env python
import sys

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t')
        values = key.split(',') + value.split(',')
        yield values

def reducer():
    agg = {}

    for values in parseInput():
        neighborhood = values[0]
        hour = values[1]
        key = neighborhood + "," + hour
        agg[key] = agg.get(key, 0) + int(values[2])
        
    for key in agg.keys():
        print '{0}\t{1}'.format(key, agg[key])
        
if __name__=='__main__':
    reducer()
