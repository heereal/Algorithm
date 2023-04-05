function solution(dots) {
    let xDots = [];
    let yDots = [];
    dots.forEach((v) => {
        xDots.push(v[0]);
        yDots.push(v[1]);
    });
    return Math.abs(Math.max(...xDots) - Math.min(...xDots)) * Math.abs(Math.max(...yDots) - Math.min(...yDots));
}