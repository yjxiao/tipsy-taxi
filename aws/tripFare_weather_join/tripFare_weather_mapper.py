#!/usr/bin/python

import sys
import os

for line in sys.stdin:
    
    line = line.strip().split(',')
        
    try:
        if (len(line) == 15):
            medallion, hack_license, vendor_id, pickup_dropoffdatetime, passenger_count, triptime_insecs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, tip_amount, total_amount = line
            print pickup_dropoffdatetime[:1] + "\t" + 'trip' + "\t" + tip_amount +  ", " + total_amount
        else:
            EST, MeanTemp, MeanVisibilityMiles,  meanWindSpeed, PrecipitationIn = line
            print EST + "\t" + 'weather' + "\t" + MeanTemp + ", " + MeanVisibilityMiles + ", " + PrecipitationIn
    except:
        pass
