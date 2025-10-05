table = [['EMPTY'] * 51 for _ in range(51)]
pointer = [[(r, c) for c in range(51)] for r in range(51)]
answer = []

def insert(r, c, v):
    r, c = pointer[r][c]
    table[r][c] = v

def update(v1, v2):
    for i in range(51):
        for j in range(51):
            if table[i][j] == v1:
                table[i][j] = v2

def merge(r1, c1, r2, c2):
    r1, c1 = pointer[r1][c1]
    r2, c2 = pointer[r2][c2]
    
    if table[r1][c1] == 'EMPTY':
        table[r1][c1] = table[r2][c2]
        
    for i in range(51):
        for j in range(51):
            if pointer[i][j] == (r2, c2):
                pointer[i][j] = (r1, c1)

def unmerge(r1, c1):
    r2, c2 = pointer[r1][c1]
    v = table[r2][c2]

    for i in range(51):
        for j in range(51):  
            if pointer[i][j] == (r2, c2):
                pointer[i][j] = (i, j)
                table[i][j] = 'EMPTY'
    
    table[r1][c1] = v

def print_value(r, c):
    r, c = pointer[r][c]
    answer.append(table[r][c])
    
def solution(commands):  
    for c in commands:
        c = c.split()
        if c[0] == 'UPDATE':
            if len(c) == 4:
                insert(int(c[1]), int(c[2]), c[3])
            else:
                update(c[1], c[2])
        elif c[0] == 'MERGE':
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]))            
        elif c[0] == 'UNMERGE':
            unmerge(int(c[1]), int(c[2]))
        elif c[0] == 'PRINT':
            print_value(int(c[1]), int(c[2]))
        
    return answer