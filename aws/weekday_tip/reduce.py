#!/usr/bin/python

import sys
import string
current_day = None
current_sum = 0
current_total = 0.0
current_tip = 0.0
tip_percent = 0.0

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    day,values = line.strip().split("\t",1)
    count,total_amount,tip_amount = values.split(',')
 
    try:
        count = int(count)
    except ValueError:
        continue
    
    if day  == current_day:
        current_sum += count
        current_total += float(total_amount)
        current_tip += float(tip_amount)
    else:
        if current_day:
            if current_total == 0:
                tip_percent = 0
            else:
                tip_percent = current_tip/current_total*100
	        print "%s\t%d\t%.2f\t%.2f" %( current_day, current_sum,current_total,tip_percent)
        current_day = day
        current_sum = count
        current_total = float(total_amount)
        current_tip = float(tip_amount)
        
if current_total == 0:
    tip_percent = 0
else:
    tip_percent = current_tip/current_total*100
print "%s\t%d\t%.2f\t%.2f" %( current_day, current_sum,current_total,tip_percent)
