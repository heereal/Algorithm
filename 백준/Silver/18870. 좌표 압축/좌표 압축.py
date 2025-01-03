import sys
input = sys.stdin.readline

N = int(input())
x_list = list(map(int, input().split()))

set_list = sorted(set(x_list))
dic = {set_list[i] : i for i in range(len(set_list))}

for i in x_list:
    print(dic[i], end=" ")