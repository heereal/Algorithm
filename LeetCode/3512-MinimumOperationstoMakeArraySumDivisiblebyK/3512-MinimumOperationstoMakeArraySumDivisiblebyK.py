# Last updated: 2026. 4. 19. 오후 10:15:20
1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        total = sum(nums)
4        answer = 0
5
6        while total % k != 0:
7            answer += 1
8            total -= 1
9        
10        return answer
11
12        