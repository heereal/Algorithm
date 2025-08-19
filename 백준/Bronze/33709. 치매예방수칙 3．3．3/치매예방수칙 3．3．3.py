n = int(input())
str = input()

for s in ['#', ':', '|']:
    str = str.replace(s, '.')

arr = [int(i) for i in str.split('.')]
print(sum(arr))