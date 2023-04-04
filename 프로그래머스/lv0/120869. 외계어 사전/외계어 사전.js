function solution(spell, dic) {
    return dic.filter((str) => str.split("").sort().join("") === spell.sort().join("")).length > 0 ? 1 : 2;
}