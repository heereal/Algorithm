function solution(hp) {
    const a = Math.floor(hp / 5)
    const b = hp % 5
    const c = Math.floor(b / 3)
    const d = b % 3
    return a + c + d
}