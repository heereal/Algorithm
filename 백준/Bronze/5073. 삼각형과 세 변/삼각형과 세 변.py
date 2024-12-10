while True:
    a, b, c = map(int, input().split())
    length_list = [a, b, c]
    length_set = len(set(length_list))
    
    if a == b == c == 0:
        break
    elif max(length_list) >= sum(length_list) - max(length_list):
        print('Invalid')
    elif length_set == 1:
        print('Equilateral')
    elif length_set == 2:
        print('Isosceles')
    elif length_set == 3:
        print('Scalene')
