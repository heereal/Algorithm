import math

A, B, V = map(int, input().split())
result = (V-B)/(A-B)
print(math.ceil(result))