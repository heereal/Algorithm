bowls = input()
height = 10
is_correct = True if bowls[0] == "(" else False

for i in range(1, len(bowls)):
    if bowls[i] == "(":
        if is_correct:
            height += 5
        else:
            height += 10
        is_correct = True
    else:
        if not is_correct:
            height += 5
        else: 
            height += 10
        is_correct = False

print(height)