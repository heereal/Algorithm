import math

a = int(input())
d = math.sqrt(a / math.pi) * 2
res = (d + 2) ** 2
print(f'{res:.10f}')