import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_keys = {i+1 : input().strip() for i in range(N)}
name_keys = {name : num for num, name in num_keys.items()}

for _ in range(M):
    q = input().strip()

    if q.isalpha():
        print(name_keys[q])
    else:
        print(num_keys[int(q)])