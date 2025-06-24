def solution(prices):
    n = len(prices)
    stack = []
    answer = [n - 1 - i for i in range(n)]
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    
    return answer