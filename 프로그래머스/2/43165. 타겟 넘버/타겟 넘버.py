def dfs(nums, target, i, res):
    global cnt
    
    if i == len(nums):
        if res == target:
            return 1
        else:
            return 0
    
    return dfs(nums, target, i+1, res+nums[i]) + dfs(nums, target, i+1, res-nums[i])

def solution(nums, target):
    return dfs(nums, target, 0, 0)
    