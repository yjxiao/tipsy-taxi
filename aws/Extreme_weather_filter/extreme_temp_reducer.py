#!/usr/bin/python

import sys
import os

current_percentage = 0
current_sum = 0

for line in sys.stdin:
    
    tip_percentage, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
        tip_percentage = float(tip_percentage)
    except ValueError:
        continue
    
    if tip_percentage == current_percentage:
        current_sum += count
    else:
        if current_percentage:
            # output goes to STDOUT (stream data that the program writes)
            print "%.4f\t%d" %( current_percentage, current_sum )
        current_percentage = tip_percentage
        current_sum = count
        
# output goes to STDOUT (stream data that the program writes)
print "%.4f\t%d" %( current_percentage, current_sum )
    