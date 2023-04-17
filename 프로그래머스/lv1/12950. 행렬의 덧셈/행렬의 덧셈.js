function solution(arr1, arr2) {
    return arr1.map((arr, first_index) => arr.map((num, second_index) => num + arr2[first_index][second_index]));
}