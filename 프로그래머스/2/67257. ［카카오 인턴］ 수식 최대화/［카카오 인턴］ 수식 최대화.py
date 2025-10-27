from itertools import permutations

def solution(expression):
    ops = ['*', '+', '-']
    order = permutations(ops, 3)
    
    arr = []
    answer = 0
    
    op_index = 0
    
    for i in range(len(expression)):
        if expression[i] in ops:
            arr += [expression[op_index:i], expression[i]]
            op_index = i + 1
            
    arr.append(expression[op_index:])
    
    for per in order:
        temp = arr[:]
        for op in per:
            for i in range(len(temp)):
                if temp[i] == op:
                    temp[i-1:i+2] = ['/', '/', str(eval("".join(temp[i-1:i+2])))]
            temp = [x for x in temp if x != '/']
            
        answer = max(answer, abs(int(temp[0])))            

    return answer