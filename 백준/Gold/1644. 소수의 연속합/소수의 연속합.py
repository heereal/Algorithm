N = int(input())
nums = [False, False] + [True]*(N-1)
primes = []

for i in range(2, int(N**0.5) + 1):
    if nums[i]:
        j = 2
        while i*j <= N:
            nums[i*j] = False
            j += 1

for i in range(N+1):
    if nums[i]:
        primes.append(i)

cnt = 0
left, right = 0, 0
sum = 2

while right < len(primes):
    if sum == N:
        cnt += 1

    if sum >= N:
        left += 1
        sum -= primes[left-1]
    elif right == len(primes)-1:
        break
    else:
        right += 1
        sum += primes[right]

print(cnt)