def solution(n, lost, reserve):
    cnt = [1] * (n+2)
    
    for i in lost:
        cnt[i] -= 1
    
    for i in reserve:
        cnt[i] += 1
    
    for i in range(n+1):
        if cnt[i] == 0 and cnt[i-1] == 2:
            cnt[i] = 1
            cnt[i-1] = 1       
        elif cnt[i] == 0 and cnt[i+1] == 2:
            cnt[i] = 1
            cnt[i+1] = 1     
            
    return n - cnt.count(0)