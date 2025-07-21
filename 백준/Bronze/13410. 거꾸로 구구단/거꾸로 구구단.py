n, k = map(int, input().split())
arr = []

for i in range(1, k+1):
    num = "".join(reversed(str(n*i)))
    arr.append(int(num))

print(max(arr))