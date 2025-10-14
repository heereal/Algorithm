def solution(numbers, hand):
    dict = {1: (1, 1), 2: (1, 2), 3: (1, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3), 7: (3, 1), 8: (3, 2), 9: (3, 3), '*': (4, 1), 0: (4, 2), '#': (4, 3)}
    
    l, r = '*', '#'
    answer = ''
    
    for n in numbers:   
        if n in [1, 4, 7]:
            answer += 'L'
            l = n
        elif n in [3, 6, 9]:
            answer += 'R'
            r = n
        else:
            next_row, next_column = dict[n]
            left = abs(dict[l][0] - next_row) + abs(dict[l][1] - next_column)
            right = abs(dict[r][0] - next_row) + abs(dict[r][1] - next_column)
            
            if left == right:
                if hand == 'right':
                    answer += 'R'
                    r = n
                else:
                    answer += 'L'
                    l = n
            elif left > right:
                answer += 'R'
                r = n
            else:
                answer += 'L'
                l = n
            
    return answer