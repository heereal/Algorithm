function solution(num) {
    let result = num;
    for ( i = 0; i <= 500; i++) {
        if (num === 1) return 0;
        if (result === 1) return i;
         if (result % 2 === 1) { 
            result = 3 * result + 1;
        } else if (result % 2 === 0) {
            result = result / 2;
        }
        if (i === 500) return -1;
    }
}