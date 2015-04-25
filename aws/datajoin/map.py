#!/usr/bin/python

import sys, os

# input comes from STDIN (stream data that goes to the program)
doc = os.path.basename(os.environ['mapreduce_map_input_file'])
doc_type = doc[:9]

for line in sys.stdin:
    
    line = line.strip().split(',')
    # skip header
    if line[0] == 'medallion':
        continue

    if doc_type == 'trip_fare':
        key = line[:4]
        value = [doc_type] + line[4:6] + line[8:9] + line[10:11]
    elif doc_type == 'trip_data':
        key = line[:3] + line[5:6]
        value = [doc_type] + line[6:]
    
    # output goes to STDOUT (stream data that the program writes)
    print "{0}\t{1}".format(','.join(key), ','.join(value))
