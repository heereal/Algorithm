def solution(nums):
    S = set(nums)
    return len(nums) // 2 if len(S) > len(nums) // 2 else len(S)