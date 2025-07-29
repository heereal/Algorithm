from itertools import combinations

def solution(number):
    answer = 0
    
    for case in combinations(number, 3):
        if sum(case) == 0:
            answer += 1
    
    return answer