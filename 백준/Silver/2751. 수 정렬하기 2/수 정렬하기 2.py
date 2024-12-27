import sys

N = int(sys.stdin.readline())
num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

print(*num_list, sep='\n')