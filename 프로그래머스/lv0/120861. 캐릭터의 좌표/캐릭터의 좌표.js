function solution(keyinput, board) {
    let start = [0, 0]
    // if ( Math.abs(start[0]) < (board[0] - 1) / 2 
    //     && Math.abs(start[1]) < (board[1] - 1) / 2 ) {
    
        for (const key of keyinput) {
            if ( Math.abs(start[0] - 1) <= (board[0] - 1) / 2 && key === "left") {
                start[0] = start[0] - 1
            } 
            if ( Math.abs(start[0] + 1) <= (board[0] - 1) / 2 && key === "right") {
                start[0] = start[0] + 1
            }
            if ( Math.abs(start[1] - 1) <= (board[1] - 1) / 2 && key === "down") {
                start[1] = start[1] - 1
            }
            if ( Math.abs(start[1]+ 1) <= (board[1] - 1) / 2 && key === "up") {
                start[1] = start[1] + 1
            }
        }
    
    
    
    return start
}