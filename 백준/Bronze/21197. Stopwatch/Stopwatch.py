N = int(input())
press = [int(input()) for _ in range(N)]

if N % 2 == 1:  
    print("still running")
else:           
    total = 0
    for i in range(0, N, 2):
        total += press[i+1] - press[i]
    print(total)