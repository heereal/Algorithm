function solution(str_list) {
    const indexL =  str_list.indexOf("l");
    const indexR = str_list.indexOf("r");
    if (indexL === -1 && indexR === -1) return [];
    if (indexL === -1) return str_list.slice(indexR + 1);
    if (indexR === -1) return str_list.slice(0, indexL);
    return indexL < indexR ? str_list.slice(0, indexL) : str_list.slice(indexR + 1);
}