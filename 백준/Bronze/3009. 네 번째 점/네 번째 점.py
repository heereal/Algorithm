point_list = [[], []]
for i in range(3):
    x, y = map(int, input().split())
    point_list[0].remove(x) if x in point_list[0] else point_list[0].append(x)
    point_list[1].remove(y) if y in point_list[1] else point_list[1].append(y)

print(point_list[0][0], point_list[1][0])