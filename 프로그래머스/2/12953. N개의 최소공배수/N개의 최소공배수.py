def solution(arr):
    arr.sort()
    cnt = 0
    
    while True:
        cnt += 1
        lcm = arr[-1] * cnt
        is_possible = True
        
        for num in arr:
            if lcm % num != 0:
                is_possible = False
                break
                
        if is_possible:
            break
    
    return arr[-1] * cnt