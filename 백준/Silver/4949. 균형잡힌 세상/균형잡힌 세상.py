while True:
    str = input()

    if str == ".":
        break
    
    li = []
    for i in str:
        if i in "()[]":
            li.append(i)

    s = "".join(li)
    while True:

        if s == "":
            print("yes")
            break
        elif "()" not in s and "[]" not in s:
            print("no")
            break
        else:
            s = s.replace("()", "")
            s = s.replace("[]", "")
