function solution(A, B) {
    let array = A.split("");
    if ( A === B ) return 0;
    for ( i = 1; i <= A.length; i++ ) {
        let slice = array.slice(0,A.length-1);
        slice.unshift(array[array.length-1]);
        array = slice;
        if ( slice.join("") === B ) return i   
        if ( i === A.length && slice.join("") !== B) return -1
    }
}