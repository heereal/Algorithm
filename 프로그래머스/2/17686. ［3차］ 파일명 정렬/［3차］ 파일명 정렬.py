def solution(files):
    answer = []
    
    for file in files:
        head, number, tail = '', '', ''
        
        for i, s in enumerate(file):
            if s.isdigit():
                number += s
            elif not number:
                head += s
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))            
            
    return [''.join(x) for x in answer]