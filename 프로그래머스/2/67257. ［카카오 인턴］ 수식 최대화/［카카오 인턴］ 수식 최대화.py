from itertools import permutations

def solution(expression):
    ops = ['*', '+', '-']
    order = permutations(ops, 3)
    
    arr = []
    answer = 0
    
    op_index = 0
    
    for i in range(len(expression)):
        if expression[i] in ops:
            arr += [int(expression[op_index:i]), expression[i]]
            op_index = i + 1
            
    arr.append(int(expression[op_index:]))
    
    for per in order:
        temp = arr[:]
        for op in per:
            for i in range(len(temp)):
                if temp[i] == op:
                    if op == '*':
                        temp[i-1:i+2] = ['/', '/', temp[i-1] * temp[i+1]]
                    elif op == '+':
                        temp[i-1:i+2] = ['/', '/', temp[i-1] + temp[i+1]]
                    elif op == '-':
                        temp[i-1:i+2] = ['/', '/', temp[i-1] - temp[i+1]]
            temp = [x for x in temp if x != '/']
            
        answer = max(answer, abs(temp[0]))            

    return answer