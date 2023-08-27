function solution(s) {
    let arr = s.split(" ");
    for (let i = 0; i < arr.length; i++) {
        let arr2 = arr[i].split("");
        for (let j = 0; j < arr2.length; j++) {
            const regex = /[1234567890]/;
            if (regex.test(arr[i][j])) continue;
            if (j === 0) {
                arr2[j] = arr2[j].toUpperCase();
                continue;
            };
            if (j !== 0) arr2[j] = arr2[j].toLowerCase();      
            }
        arr[i] = arr2.join("");
        }
    return arr.join(" ");
}