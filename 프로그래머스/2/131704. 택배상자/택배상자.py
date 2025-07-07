from collections import deque

def solution(order):
    main_first_box = 1
    sub = []
    answer = 0
    
    for box in order:
        if box not in sub and box >= main_first_box:
            temp = [i for i in range(main_first_box, box + 1)]
            sub += temp
            main_first_box = box + 1

        if sub.pop() == box:
            answer += 1
        else:
            break
 
    return answer