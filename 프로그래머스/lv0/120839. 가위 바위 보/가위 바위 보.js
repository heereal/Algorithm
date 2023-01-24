function solution(rsp) {
    let answer = "";
    for (const num of rsp) {
        if ( num === "2") {
            answer += "0"
        } else if ( num === "0" ) {
            answer += "5"
        } else if ( num === "5" ) {
            answer += "2"
        } 
    }
    return answer;
}