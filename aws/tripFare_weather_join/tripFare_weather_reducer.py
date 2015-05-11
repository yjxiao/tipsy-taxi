#!/usr/bin/python

import sys

join_key = None
value_trip = []
value_weather = []
current_file = None

for line in sys.stdin:
    
    key, file, value = line.strip().split('\t')
     
    if key == join_key:
        if file == 'trip':
            value_trip.append(value)
        elif file == 'weather':
            value_weather.append(value)
    else:
        if join_key:
            for i in value_trip:
                for j in value_weather:
                    print join_key + ', ' + i + ', ' + j
        
        join_key = key
        value_trip = []
        value_weather = []
        if file == 'trip':
            value_trip.append(value)
        elif file == 'weather':
            value_weather.append(value)

for i in value_trip:
    for j in value_weather:
        print join_key + ', ' + i + ', ' + j