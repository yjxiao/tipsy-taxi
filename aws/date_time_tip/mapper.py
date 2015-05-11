#!/usr/bin/env python
import sys
sys.path.append('.')
from datetime import date
import numpy

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t', 1)
        values = key.split(',') + value.split(',')
        if len(values) > 1:
            yield values

def mapper():

    tip_agg = {}
    fare_agg = {}
    for values in parseInput():
        dt = values[3]
        if dt:
            d, t = dt.strip().split()
            hour = t[:2]
            wd = date(*map(int, d.split('-'))).isoweekday()
            key = str(wd) + ',' + hour
            tip = float(values[14])
            fare = float(values[13])
            tip_agg[key] = tip_agg.get(key, 0) + tip
            fare_agg[key] = fare_agg.get(key, 0) + fare

    for key in tip_agg.keys():
        print '{0}\t{1},{2}'.format(key, tip_agg[key], fare_agg[key])

if __name__=='__main__':
    mapper()
