#!/usr/bin/env python
from __future__ import division
import sys
sys.path.append('.')

def mapper():
    agg = {}
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split('\t', 1)[1].split(',')
        try:
            fare = float(values[9])
            tip = float(values[10])
            dist = float(values[3])
        except:
            continue
        try:
            pct = int(tip * 100 / fare)
        except ZeroDivisionError:
            continue
        dist = int(dist)
        key = "{0},{1}".format(pct, dist)
        agg[key] = agg.get(key, 0) + 1

    for key in agg:
        print '{0}\t{1}'.format(key, agg[key])

if __name__=='__main__':
    mapper()
