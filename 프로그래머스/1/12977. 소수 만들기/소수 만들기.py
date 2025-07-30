from itertools import combinations

def is_decimal(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for c in combinations(nums, 3):
        res = is_decimal(sum(c))
        if res:
            answer += 1
    
    return answer