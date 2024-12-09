a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    angle_set = len(set([a, b, c]))  
    if angle_set == 3:
        print('Scalene')
    elif angle_set == 2:
        print('Isosceles')
    elif angle_set == 1:
        print('Equilateral')
else:
    print('Error')