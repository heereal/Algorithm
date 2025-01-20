import sys
input = sys.stdin.readline

max = 1000000
nums = [True]*(max+1)

for i in range(2, int(max**0.5)+1):
    if nums[i]:
        for j in range(i*2, max+1, i):
            nums[j] = False

T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0

    for i in range(2, N//2+1):
        if nums[i] and nums[N-i]:
            cnt += 1
    
    print(cnt)