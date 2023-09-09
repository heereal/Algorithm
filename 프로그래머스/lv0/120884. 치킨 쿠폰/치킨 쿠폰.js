function solution(chicken) {
    let freeChicken = 0;
    while (chicken >= 10) {
        freeChicken += Math.floor(chicken / 10);
        chicken = Math.floor(chicken / 10) + (chicken % 10);
    }
    return freeChicken;
}