import sys
input = sys.stdin.readline

N = int(input())
my_list = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

dic = {my_list[i] : 1 for i in range(len(my_list))}

for i in check_list:
    if i in dic:
        print(1, end=" ")
    else:
        print(0, end=" ")