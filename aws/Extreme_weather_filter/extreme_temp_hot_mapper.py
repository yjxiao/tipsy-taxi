#!/usr/bin/python

import sys
import os

dateList = ['2013-05-31', '2013-06-01', '2013-06-24', '2013-06-25',
       '2013-07-05', '2013-07-06', '2013-07-07', '2013-07-14',
       '2013-07-15', '2013-07-16', '2013-07-17', '2013-07-18',
       '2013-07-19', '2013-07-20', '2013-07-21', '2013-09-11']
	   
for line in sys.stdin:
    
    line = line.strip().split(',')

    
    date, tip_amount, total_amount, MeanTemp, MeanVisibilityMiles, PrecipitationIn = line
    try:
        tip_amount, total_amount = float(tip_amount), float(total_amount)
        tip_percentage = float(tip_amount) / float(total_amount)
        if date in dateList:
            print "%.4f\t%d" %(tip_percentage , 1 )
    except:
        pass	