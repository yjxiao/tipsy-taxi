#!/usr/bin/env python
import sys

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t')
        values = [key] + value.split(',')
        yield values

def reducer():
    tip_agg = {}
    fare_agg = {}
    for values in parseInput():
        neighborhood = values[0]
        tip = float(values[1])
        fare = float(values[2])
        tip_agg[neighborhood] = tip_agg.get(neighborhood, 0) + tip
        fare_agg[neighborhood] = fare_agg.get(neighborhood, 0) + fare        
        
    for neighborhood in tip_agg.keys():
        print '{0}\t{1}'.format(neighborhood, tip_agg[neighborhood] / fare_agg[neighborhood])
        
if __name__=='__main__':
    reducer()
