function solution(myString, pat) {
    const index = myString.lastIndexOf(pat) + pat.length
    return myString.slice(0, index);
}