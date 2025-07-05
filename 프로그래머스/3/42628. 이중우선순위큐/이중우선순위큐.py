def solution(operations):
    heap = []
    
    for op in operations:
        if "I" in op:
            _, num = op.split(" ")
            heap.append(int(num))
        elif op == "D 1" and heap:
            heap.remove(max(heap))
        elif op == "D -1" and heap:
            heap.remove(min(heap))
    
    if not heap:
        return [0, 0]
    else:
        return [max(heap), min(heap)]