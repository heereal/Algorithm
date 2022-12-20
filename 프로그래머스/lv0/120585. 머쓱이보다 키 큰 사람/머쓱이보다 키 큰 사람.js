function solution(array, height) {
    return array.filter((person) => person > height).length
}