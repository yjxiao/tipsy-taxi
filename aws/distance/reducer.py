#!/usr/bin/env python
import sys
sys.path.append('.')

def reducer():

    agg = {}
    for line in sys.stdin:
        key, cnt = line.strip('\n').split('\t', 1)
        cnt = int(cnt)
        agg[key] = agg.get(key, 0) + cnt

    for key in agg:
        print '{0}\t{1}'.format(key, agg[key])

if __name__=='__main__':
    reducer()
