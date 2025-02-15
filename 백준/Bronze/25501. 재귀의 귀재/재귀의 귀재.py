import sys
input = sys.stdin.readline

N = int(input())

def recursion(str, cnt, l, r):
    if l >= r:
        return f'1 {cnt}'
    elif str[l] != str[r]:
        return f'0 {cnt}'
    else:
        return recursion(str, cnt+1, l+1, r-1)


for _ in range(N):
    str = input().strip()
    print(recursion(str, 1, 0, len(str)-1))