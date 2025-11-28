while True:
    n = int(input())

    if n == -1:
        break

    clays = []

    for  i in range(n):
        x, y, z, name = input().split()
        clays.append((int(x) * int(y) * int(z), name))
    
    bully = max(clays)[1]
    victim = min(clays)[1]
    
    print(f'{bully} took clay from {victim}.')