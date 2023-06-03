function solution(arr, query) {
  let start = 0;
  let end = arr.length;
  for (let i = 0; i < query.length; i++) {
    i % 2 ? start += query[i] : end = start + query[i];
  }
  return arr.slice(start, end + 1);
}