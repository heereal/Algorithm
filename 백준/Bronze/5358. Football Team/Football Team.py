pair = {'i': 'e', 'e': 'i', 'I': 'E', 'E': 'I'}

while True:
    try: 
        name = list(input())

        for i, s in enumerate(name):
            if s in pair:
                name[i] = pair[s]
    
        print("".join(name))
    except:
        break