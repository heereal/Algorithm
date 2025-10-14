keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

def get_row(n):
    for i, line in enumerate(keypad):
        if n in line:
            return i

def solution(numbers, hand):
    keypad = [2, 5, 8, 11]
    column = [3, 1, 2]
    
    l, r = 10, 12
    answer = ''
    
    for n in numbers:   
        if n == 0:
            n = 11
      
        if n in [1, 4, 7]:
            answer += 'L'
            l = n
        elif n in [3, 6, 9]:
            answer += 'R'
            r = n
        else:
            next_row = keypad.index(n)
            next_column = column[n % 3]
            
            left = abs(get_row(l) - next_row) + abs(column[l % 3] - next_column)
            right = abs(get_row(r) - next_row) + abs(column[r % 3] - next_column)
            
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