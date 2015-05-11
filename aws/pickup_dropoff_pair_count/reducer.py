#!/usr/bin/env python
import sys

def parseInput():
    for line in sys.stdin:
        values = line.strip('\n').split('\t')
        yield values

def reducer():
    agg = {}

    for values in parseInput():
        pair = values[0]
        agg[pair] = agg.get(pair, 0) + int(values[1])
        
    for key in agg.keys():
        print '{0}\t{1}'.format(key, agg[key])
        
if __name__=='__main__':
    reducer()
