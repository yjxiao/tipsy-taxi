#!/usr/bin/env python

import sys
from datetime import datetime

for line in sys.stdin:

    line = line.strip()

    key,value = line.split('\t',1)
    values = value.split(',')
    dropoff_datetime = datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S")
    #weekday(): integer 0-6 <==> Monday, Tuesday,...,Satuday,Sunday
    dropoff_day = dropoff_datetime.weekday()
    tip_amount = float(values[-2])
    total_amount = float(values[-1]) 
    
    print "%s\t%d,%s,%s" %(dropoff_day,1,total_amount,tip_amount) 
