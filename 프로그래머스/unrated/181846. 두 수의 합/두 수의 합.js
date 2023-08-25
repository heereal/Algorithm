const a = "18446744073709551615";
const b = "287346502836570928366";

function solution(a, b) {
    return (BigInt(a) + BigInt(b)).toString();
}