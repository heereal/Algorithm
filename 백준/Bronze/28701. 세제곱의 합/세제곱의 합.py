n = int(input())
arr = [i for i in range(1, n+1)]

print(sum(arr))
print(sum(arr)**2)

answer = 0
for i in arr:
    answer += i**3

print(answer)