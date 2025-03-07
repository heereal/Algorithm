N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(cnt, res):
    global mx, mn

    if cnt == N-1:
        mx = max(mx, res)
        mn = min(mn, res)
        return

    if ops[0] > 0: 
        ops[0] -= 1
        dfs(cnt+1, res + nums[cnt+1])
        ops[0] += 1
        
    if ops[1] > 0: 
        ops[1] -= 1
        dfs(cnt+1, res - nums[cnt+1])
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        dfs(cnt+1, res * nums[cnt+1])
        ops[2] += 1

    if ops[3] > 0: 
        ops[3] -= 1
        dfs(cnt+1, int(res / nums[cnt+1]))
        ops[3] += 1

dfs(0, nums[0])

print(int(mx))
print(int(mn))