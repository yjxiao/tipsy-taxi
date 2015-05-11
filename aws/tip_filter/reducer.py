#!/usr/bin/env python
import sys
sys.path.append('.')

def reducer():
    for line in sys.stdin:
        line = line.strip('\n')
        print line

if __name__=='__main__':
    reducer()
