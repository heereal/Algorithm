H, M = map(int, input().split())
timer = int(input())

total_minute = M + timer
H += total_minute // 60
M = total_minute % 60

if H > 23:
    H -= 24

print(H, M)