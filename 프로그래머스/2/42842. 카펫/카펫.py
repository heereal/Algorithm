def solution(brown, yellow):
    area = brown + yellow
    width = area - 2
    
    while True:
        width -= 1
        
        if area % width == 0:
            height = area // width
            
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
                break