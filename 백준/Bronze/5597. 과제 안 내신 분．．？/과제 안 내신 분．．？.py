students = [i for i in range(1, 31)]
for _ in range(28):
    n = int(input())
    students.remove(n)

for n in students:
    print(n)
