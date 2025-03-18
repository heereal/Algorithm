def solution(nums, target):
    leaves = [0] # 모든 계산 결과를 담음
    cnt = 0
    
    for num in nums:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
       
        leaves = temp
        
    for leaf in leaves:
        if leaf == target:
            cnt += 1
    
    return cnt
    