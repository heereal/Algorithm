function solution(s){
    let p = 0;
    let y = 0;
    s.split("").filter((str) => str.toLowerCase() === "p" ? p += 1 : str.toLowerCase() === "y" ? y += 1 : null )
    return p === y ? true : false 
}