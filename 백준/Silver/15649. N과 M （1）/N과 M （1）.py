N, M = map(int, input().split())

nums = []
visited = [False]*(N+1)

def backtracking():
    if len(nums) == M:
        print(*nums)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            nums.append(i)
            visited[i] = True
            backtracking()

            nums.pop()
            visited[i] = False
            
backtracking()