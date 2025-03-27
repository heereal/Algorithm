def solution(n):
    num = n
    divisions = []
    
    while True:
        if num // 2 <= 1:
            break
        else:
            num = num // 2
            divisions.append(num)
    
    divisions.sort()
    power = 2 if (n % 2 and n > 1) else 1 # 건전지 사용량
    now = 1 # 현재 위치
    
    for next in divisions:
        if now*2 != next:
            power += next - (now*2)
            
        now = next
         
    return power