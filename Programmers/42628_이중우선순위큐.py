def solution(operations):
    heap = []
    for op in operations:
        command, num = op.split()[0], int(op.split()[1])
        if command == 'I':
            heap.append(num)
        elif heap and command == 'D':
            if num == 1:
                heap.pop(heap.index(max(heap)))
            else:
                heap.pop(heap.index(min(heap)))
    if not heap:
        return [0, 0]
    else:
        return [max(heap), min(heap)]
