#!/usr/bin/python

import sys
import os
	   
for line in sys.stdin:
    
    line = line.strip().split(',')

    
    date, tip_amount, total_amount, MeanTemp, MeanVisibilityMiles, PrecipitationIn = line
    try:
        tip_amount, total_amount = float(tip_amount), float(total_amount)
        tip_percentage = float(tip_amount) / float(total_amount)
        if float(PrecipitationIn) >= 1.5:
            print "%.4f\t%d" %(tip_percentage , 1 )
    except:
        pass