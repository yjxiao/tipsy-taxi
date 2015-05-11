#!/usr/bin/env python
import sys
sys.path.append('.')

def mapper():
    is_qualified = lambda x: x in set(['2013000366', '2013023538', '2013000946', '2013008631', '2013028741'])
    for line in sys.stdin:
        line = line.strip('\n')
        key = line.split('\t', 1)[0]
        driver = key.split(',')[1]
        if is_qualified(driver):
            print line

if __name__=='__main__':
    mapper()
