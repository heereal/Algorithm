def solution(sizes):
	return max(max(x) for x in sizes) * max(min(y) for y in sizes)