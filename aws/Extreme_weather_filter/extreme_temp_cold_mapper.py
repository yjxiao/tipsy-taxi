#!/usr/bin/python

import sys
import os

dateList = ['2013-01-02', '2013-01-03', '2013-01-18', '2013-01-21',
       '2013-01-22', '2013-01-23', '2013-01-24', '2013-01-25',
       '2013-01-26', '2013-01-27', '2013-02-01', '2013-02-02',
       '2013-02-03', '2013-02-04', '2013-02-05', '2013-02-07',
       '2013-02-08', '2013-02-09', '2013-02-10', '2013-02-17',
       '2013-02-18', '2013-02-20', '2013-02-21', '2013-02-22',
       '2013-03-18', '2013-11-24', '2013-11-25', '2013-11-30',
       '2013-12-08', '2013-12-11', '2013-12-12', '2013-12-13',
       '2013-12-14', '2013-12-16', '2013-12-17', '2013-12-18',
       '2013-12-25', '2013-12-31']
	   
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
