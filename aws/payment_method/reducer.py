#!/usr/bin/env python
import sys
sys.path.append('.')

def reducer():
    current_type = None
    
    for line in sys.stdin:
        line = line.strip('\n').split('\t', 1)
        pay_type = line[0]
        fare, tip, cnt = map(float, line[1].strip().split(","))
        cnt = int(cnt)
        if current_type is None:
            current_type = pay_type
            fare_agg = fare
            tip_agg = tip
            cnt_agg = cnt
        elif current_type == pay_type:
            fare_agg += fare
            tip_agg += tip
            cnt_agg += cnt
        else:
            try:
                pct = tip_agg / fare_agg
            except ZeroDivisionError:
                continue
            print '{0}\t{1},{2}'.format(current_type, pct, cnt_agg)
            current_type = pay_type
            fare_agg = fare
            tip_agg = tip
            cnt_agg = cnt

    try:
        pct = tip_agg / fare_agg
    except ZeroDivisionError:
        pct = 0

    print '{0}\t{1},{2}'.format(current_type, pct, cnt_agg)

if __name__=='__main__':
    reducer()
