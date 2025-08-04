def get_grade(cnt):
    if cnt <= 1:
        return 6
    else:
        return 7 - cnt

def solution(lottos, win_nums):
    lowest = 0
    
    for num in lottos:
        if num in win_nums:
            lowest += 1
    
    return [get_grade(lowest + lottos.count(0)), get_grade(lowest)]