function solution(score) {
    const average_array = score.map((item) => (item[0] + item[1]) / 2)
    const sorted_array = [...average_array].sort((a,b) => b-a)
    return average_array.map((v) => sorted_array.indexOf(v)+1)
}