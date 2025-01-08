import sys
input = sys.stdin.readline

n = int(input())
my_list = map(int, input().split())
m = int(input())
card_list = map(int, input().split())

dic = {}
for i in my_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in card_list:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")