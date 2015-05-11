#!/usr/bin/env python
from __future__ import division
import sys
sys.path.append('.')

def mapper():
    
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split('\t', 1)[1].split(',')
        fare = float(values[9])
        tip = float(values[10])
        try:
            percentage = tip / fare * 100
        except ZeroDivisionError:
            continue
        
        print '{0}\t1'.format(int(percentage))

if __name__=='__main__':
    mapper()
