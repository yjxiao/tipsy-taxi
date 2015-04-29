#!/usr/bin/env python
import sys
sys.path.append('.')
import numpy

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t', 1)
        values = key.split(',') + value.split(',')
        if len(values) > 1:
            yield values

def mapper():
    tip_agg = 0
    fare_agg = 0
    count = 0
    current = None
    for values in parseInput():
        tip = float(values[14])
        fare = float(values[13])
        driver = values[1]
        if current is None:
            current = driver
            tip_agg = tip
            fare_agg = fare
            count = 1
        elif driver == current:
            tip_agg += tip
            fare_agg += fare
            count += 1
        else:
            print '{0}\t{1},{2},{3}'.format(driver, tip_agg, fare_agg, count)
            current = driver
            tip_agg = tip
            fare_agg = fare
            count = 1
                                                                        
    print '{0}\t{1},{2},{3}'.format(driver, tip_agg, fare_agg, count)

if __name__=='__main__':
    mapper()
