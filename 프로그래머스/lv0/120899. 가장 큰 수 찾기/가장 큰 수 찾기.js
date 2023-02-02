function solution(array) {
    let max_num = array[0];
    let answer = [];
    for (const i in array) {
      if (array[i] > max_num) {
          max_num = array[i];
          answer = [max_num, +i];
      }
    }
    return answer;
}