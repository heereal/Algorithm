while True:
    word = input()
    stack = []

    if word == ".":
        break

    for str in word:
        if str in "([":
            stack.append(str)

        elif str == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(str)
                break
        
        elif str == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(str)
                break
    
    if stack:
        print("no")
    else:
        print("yes")