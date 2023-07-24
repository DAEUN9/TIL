def solution(sizes):
    answer = 0
    a, b = 0, 0
    for x, y in sizes:
        if x >= y:
            a = max(a, x)
            b = max(b, y)
        else:
            a = max(a, y)
            b = max(b, x)
    return a*b