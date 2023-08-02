function solution(n_str) {
    if (!/^0+/.test(n_str)) return n_str;
    if (/^0+/.test(n_str)) {
        const arr = [...n_str];
        for (const i in arr) {
            if (arr[i] !== "0") return arr.slice(i).join("");
        };
    };
}