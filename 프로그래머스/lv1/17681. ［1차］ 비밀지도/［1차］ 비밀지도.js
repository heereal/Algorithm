function solution(n, arr1, arr2) {
    const getBinary = (arr) => {
        const result = arr.map((v) => {
            const binary = v.toString(2);
            return binary.length !== n ? "0".repeat(n - binary.length) + binary : binary
        });
        return result;
    }
    
    const binaryArr1 = getBinary(arr1);
    const binaryArr2 = getBinary(arr2);
    
    let answer = [];
    
    for (const i in binaryArr1) {
        const arr = binaryArr1[i].split("").map((item, j) => item === "1" || binaryArr2[i][j] === "1" ? "#" : " ");
        answer.push(arr.join(""));
    }
    
    return answer;
}