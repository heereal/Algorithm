function solution(s) {
    let arr = s.split(" ");
    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i].charAt(0).toUpperCase() + arr[i].substring(1).toLowerCase()
    }
    return arr.join(" ");
}