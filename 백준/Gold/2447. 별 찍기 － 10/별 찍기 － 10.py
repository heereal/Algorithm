N = int(input())

def append_star(len):
    if len == 1:
        return ['*']

    Stars = append_star(len//3)
    li = []

    for S in Stars:
        li.append(S*3)
    for S in Stars:
        li.append(S + ' '*(len//3) + S)
    for S in Stars:
        li.append(S*3)
    
    return li

print('\n'.join(append_star(N)))