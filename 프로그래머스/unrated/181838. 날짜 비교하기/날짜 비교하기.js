function solution(date1, date2) {
    for (const i in date1) {
        if (date1[i] > date2[i]) return 0;
        if (date1[i] < date2[i]) return 1;
    }
    return 0;
}