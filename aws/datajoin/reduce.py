#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
current_key = None
current_dict = {}

for line in sys.stdin:

    key, value = line.strip().split("\t", 1)
    value = value.split(',')
    doc_type = value[0]
    if key == current_key:
        if doc_type not in current_dict:
            current_dict[doc_type] = [value[1:]]
        else:
            current_dict[doc_type].append(value[1:])
    
    else:
        if current_key:
            if ('trip_fare' in current_dict) and ('trip_data' in current_dict):
                for t in current_dict['trip_data']:
                    for f in current_dict['trip_fare']:
                        v = ','.join(t) + ',' + ','.join(f)
                        print "{0}\t{1}".format(current_key, v)

        current_key = key
        current_dict = {doc_type: [value[1:]]}
        
# output goes to STDOUT (stream data that the program writes)
if ('trip_fare' in current_dict) and ('trip_data' in current_dict):
    for t in current_dict['trip_data']:
        for f in current_dict['trip_fare']:
            v = ','.join(t) + ',' + ','.join(f)
            print "{0}\t{1}".format(current_key, v)

