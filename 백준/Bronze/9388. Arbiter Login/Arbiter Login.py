n = int(input())

for i in range(n):
    o, v = input().split()
    only_str = (''.join(char for char in o if not char.isnumeric()))

    if o == v:
        print(f'Case {i+1}: Login successful.')
    elif o == v.swapcase():
        print(f'Case {i+1}: Wrong password. Please, check your caps lock key.')
    elif only_str == v:
        print(f'Case {i+1}: Wrong password. Please, check your num lock key.')
    elif only_str.swapcase() == v:
        print(f'Case {i+1}: Wrong password. Please, check your caps lock and num lock keys.')
    else:
        print(f'Case {i+1}: Wrong password.')