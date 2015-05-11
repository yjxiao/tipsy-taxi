#!/usr/bin/env python
from __future__ import division
import sys
sys.path.append('.')

def mapper():
    threshold = 0.3
    
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split('\t', 1)[1].split(',')
        fare = float(values[9])
        tip = float(values[10])
        try:
            percentage = tip / fare
        except ZeroDivisionError:
            continue
        if percentage > threshold:
            print line

if __name__=='__main__':
    mapper()
