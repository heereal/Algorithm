def solution(wallpaper):
    width, height = len(wallpaper[0]), len(wallpaper)
    lux, luy, rdx, rdy = height, width, 0, 0
    
    for i in range(height):
        for j in range(width):
            if wallpaper[i][j] == "#":
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i+1)
                rdy = max(rdy, j+1)
        
    return [lux, luy, rdx, rdy]