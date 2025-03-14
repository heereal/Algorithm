N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_length = N + 1

while True:
    if sum >= S:
        min_length = min(min_length, right-left)
        sum -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        sum += nums[right]
        right += 1

result = 0 if min_length == N + 1 else min_length
print(result)