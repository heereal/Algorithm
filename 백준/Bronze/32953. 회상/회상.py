n, m = map(int, input().split())
dic = {}
answer = 0

for _ in range(n):
    k = int(input())
    students = list(input().split())
    
    for number in students:
        if number in dic:
            dic[number] += 1
        else:
            dic[number] = 1

print(len(list(filter(lambda x: x >= m, dic.values()))))