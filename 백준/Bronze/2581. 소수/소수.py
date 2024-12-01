M = int(input())
N = int(input())
num_list = []

for num in range(M, N+1):
    if num > 1:
        is_prime = True
        for i in range(2, num): 
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            num_list.append(num)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])
