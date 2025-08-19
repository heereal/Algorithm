n = int(input())
res = []

for _ in range(n):
    j, m = map(int, input().split())
    win_num = (j - 1) % (m + 1)
    cnt = 0
    
    for _ in range(win_num, j + 1, m + 1):
        cnt += 1
        
    res.append(cnt)

min_turn = min(res)
print(res.index(min_turn) + 1, min_turn * 2)