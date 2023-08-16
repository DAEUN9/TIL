def solution(brown, yellow):
    answer = []
    for y in range(1, brown+1):
        for x in range(y, brown+1):
            if 2*x + 2*y - 4 == brown:
                if (x-2) * (y-2) == yellow:
                    return [x, y]
    return answer