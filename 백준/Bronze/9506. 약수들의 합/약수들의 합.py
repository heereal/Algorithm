while True:
    n = int(input())
    if n == -1:
        break

    num_list = []
    for i in range(1, n):
        if n % i == 0:
            num_list.append(i)
    
    if sum(num_list) == n:
        temp = " + ".join(str(i) for i in num_list)
        print(f"{n} = {temp}")
    else:
        print(f"{n} is NOT perfect.")