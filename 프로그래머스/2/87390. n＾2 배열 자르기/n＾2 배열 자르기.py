def solution(n, left, right):
    arr = []
    
    for i in range(left, right + 1):
        row = i // n 
        column = i % n
        v = max(row, column) + 1
        arr.append(v)
            
    return arr