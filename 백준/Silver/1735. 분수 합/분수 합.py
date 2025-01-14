a, b = map(int, input().split())
c, d = map(int, input().split())

top = a*d + b*c
bottom = b*d

tt = top
bb = bottom

while bottom > 0:
    top, bottom = bottom, top%bottom

print(tt//top, bb//top)