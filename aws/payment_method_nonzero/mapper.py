#!/usr/bin/env python
from __future__ import division
import sys
sys.path.append('.')

def mapper():
    
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split('\t', 1)[1].split(',')
        pay_type = values[8]
        fare = float(values[9])
        tip = float(values[10])
        if tip > 0.01:        
            print '{0}\t{1},{2},1'.format(pay_type, fare, tip)

if __name__=='__main__':
    mapper()
