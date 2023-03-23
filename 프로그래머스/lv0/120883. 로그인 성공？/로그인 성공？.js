function solution(id_pw, db) {
    return db.find((item) => item[0] === id_pw[0] && item[1] === id_pw[1]) 
        ? "login" 
        : db.find((item) => item[0] === id_pw[0]) 
        ? "wrong pw" 
        : "fail"
}