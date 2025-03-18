def solution(nums, target):
    cnt = 0
    
    def dfs(i, res):
        if i == len(nums):
            if res == target:
                nonlocal cnt
                cnt += 1
            return
        
        for op in ["+", "-"]:
            if op == "+":
                res += nums[i]
                dfs(i+1, res)
                res -= nums[i]
            else:
                res -= nums[i]
                dfs(i+1, res)
    
    dfs(0, 0)
    
    return cnt