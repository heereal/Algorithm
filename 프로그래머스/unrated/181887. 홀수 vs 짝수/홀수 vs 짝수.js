function solution(num_list) {
    const result = num_list.reduce((acc, cur, index) => {
        if ( index % 2 === 0) acc[0] += cur;
        if ( index % 2 !== 0) acc[1] += cur;
        return acc;
    }, [0, 0])
    const [even, odd] = result;
    return even >= odd ? even : odd;
}