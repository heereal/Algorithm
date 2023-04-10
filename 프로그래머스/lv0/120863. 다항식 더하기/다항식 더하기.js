function solution(polynomial) {
    const array = polynomial.split(" ").filter((v) => v !== "+");
    const answer = array.reduce((acc, cur) =>  {
        if ( cur.includes("x") ) {
            cur.length === 1 ? acc[0] += 1 : acc[0] += parseInt(cur)
        } else if ( !isNaN(parseInt(cur)) ) {
            acc[1] += parseInt(cur)
        }
        return acc
    }, [0,0])
    return (answer[0] ? answer[0] === 1 ? "x" : answer[0] + "x" : "") 
        + (answer.includes(0) ? "" : " + ") 
        + (answer[1] ? answer[1] : "");
}