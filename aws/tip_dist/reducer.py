#!/usr/bin/env python
import sys
sys.path.append('.')

def reducer():
    current_pct = None
    for line in sys.stdin:
        line = line.strip('\n').split('\t')
        pct = line[0]
        if current_pct is None:
            current_pct = pct
            cnt = 1
        elif current_pct == pct:
            cnt += 1
        else:
            print '{0}\t{1}'.format(current_pct, cnt)
            current_pct = pct
            cnt = 1

    print '{0}\t{1}'.format(current_pct, cnt)


if __name__=='__main__':
    reducer()
