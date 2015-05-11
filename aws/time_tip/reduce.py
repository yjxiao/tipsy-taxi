#!/usr/bin/python

import sys
import string
from datetime import datetime
current_time = None
current_sum = 0
current_total = 0.0
current_tip = 0.0
tip_percent = 0.0
time_list = [str(datetime.strptime(str(i).zfill(2), '%H').time()) for i in range(1,24)]
time_list.append(str(datetime.strptime('23:59:59', '%H:%M:%S').time()))
print len(time_list)
i = 0
# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    time,values = line.strip().split("\t",1)
    count,total_amount,tip_amount = values.split(',')
    current_time = time_list[i]
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if time  <= current_time:
        current_sum += count
        current_total += float(total_amount)
        current_tip += float(tip_amount)
    else:
        if current_time:
            if current_total == 0:
                tip_percent = 0
            else:
                tip_percent = current_tip/current_total*100
	        print "%s\t%d\t%.2f\t%.2f" %( current_time, current_sum,current_total,tip_percent)
        i = i + 1
        current_time = time_list[i]
        current_sum = count
        current_total = float(total_amount)
        current_tip = float(tip_amount)
        
if current_total == 0:
    tip_percent = 0
else:
    tip_percent = current_tip/current_total*100
print "%s\t%d\t%.2f\t%.2f" %( current_time, current_sum,current_total,tip_percent)
