from collections import defaultdict
import math

def solution(fees, records):
    free_time, free_fee, minute, fee = fees
    cur = defaultdict(int)
    total = defaultdict(int)
    answer = []
    
    for record in records:
        time, car, type = record.split()
        h, m = map(int, time.split(':'))
        cur_minute = (h * 60) + m
        
        if type == 'IN':
            cur[car] = cur_minute
        else:
            service_minute = cur_minute - cur[car]
            total[car] += service_minute
            cur[car] = -1
    
    for car in cur:
        if cur[car] != -1:
            service_minute = ((23 * 60) + 59) - cur[car]
            total[car] += service_minute

        total_fee = free_fee
        if total[car] > free_time:
            total_fee += math.ceil((total[car] - free_time) / minute) * fee
        
        answer.append((int(car), int(total_fee)))
    
    return [x[1] for x in sorted(answer)]