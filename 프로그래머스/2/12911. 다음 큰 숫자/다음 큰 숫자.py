def count_one(n):
    # n을 2진수로 변환 후 1의 개수 카운트
    count = list(bin(n)[2:]).count("1")
    return count

def solution(n):
    now = count_one(n)
    next = 0
    
    while now != next:
        n += 1
        next = count_one(n)
        
    return n