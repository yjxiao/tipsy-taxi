#!/usr/bin/env python

import sys
from datetime import datetime

for line in sys.stdin:

    line = line.strip()

    key,value = line.split('\t',1)
    values = value.split(',')
    dropoff_datetime = datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S")
    dropoff_time = dropoff_datetime.time()
    tip_amount = float(values[-2])
    total_amount = float(values[-1])
    
    
    print "%s\t%d,%s,%s" %(dropoff_time,1,total_amount,tip_amount) 
