while True:
    s = input()
    
    if s == 'EOI':
        break

    if 'nemo' in s.lower():
        print('Found')
    else:
        print('Missing')