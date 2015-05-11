#!/usr/bin/env python
from __future__ import division
import sys

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t')
        values = key.split(',') + value.split(',')
        yield values

def reducer():
    tip_agg = {}
    fare_agg = {}

    for values in parseInput():
        wd = values[0]
        hour = values[1]
        key = wd + "," + hour
        try:
            tip = float(values[2])
            fare = float(values[3])
        except:
            continue
        tip_agg[key] = tip_agg.get(key, 0) + tip
        fare_agg[key] = fare_agg.get(key, 0) + fare
        
    for key in tip_agg.keys():
        try:
            pct = tip_agg[key] / fare_agg[key]
        except ZeroDivisionError:
            pct = 0
        print '{0}\t{1}'.format(key, pct)
        
if __name__=='__main__':
    reducer()
