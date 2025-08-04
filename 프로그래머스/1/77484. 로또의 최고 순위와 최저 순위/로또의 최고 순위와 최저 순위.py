def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    match = 0
    
    for num in lottos:
        if num in win_nums:
            match += 1
    
    return [rank[match + lottos.count(0)], rank[match]]