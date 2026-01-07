n = int(input())
dp = [1, 1]

while True:
    if sum(dp) >= n:
        print(len(dp))
        break
    
    dp.append(dp[-1] + dp[-2])