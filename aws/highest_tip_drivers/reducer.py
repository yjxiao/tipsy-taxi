#!/usr/bin/env python
import sys
import heapq

def parseInput():
    for line in sys.stdin:
        key, value = line.strip('\n').split('\t')
        values = key.split(',') + value.split(',')
        yield values

def reducer():
    k = 20
    h = []
    tip_agg = 0
    fare_agg = 0
    count_agg = 0
    current = None
    for values in parseInput():
        driver = values[0]
        tip = float(values[1])
        fare = float(values[2])
        count = int(values[3])
        if current is None:
            current = driver
            tip_agg = tip
            fare_agg = fare
            count_agg = count
        elif driver == current:
            tip_agg += tip
            fare_agg += fare
            count_agg += count
        else:
            if len(h) == k:
                heapq.heappushpop(h, (tip_agg/fare_agg, count_agg, current))
            else:
                heapq.heappush(h, (tip_agg/fare_agg, count_agg, current))
            current = driver
            tip_agg = tip
            fare_agg = fare
            count_agg = count
            
    if len(h) == k:
        heapq.heappushpop(h, (tip_agg/fare_agg, count_agg, current))
    else:
        heapq.heappush(h, (tip_agg/fare_agg, count_agg, current))
    
    for records in heapq.nlargest(k, h):
        print '{0}\t{1},{2}'.format(records[2], records[0], records[1])
        
if __name__=='__main__':
    reducer()
