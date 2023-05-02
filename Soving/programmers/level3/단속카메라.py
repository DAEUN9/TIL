def solution(routes):
    routes.sort(key=lambda x : x[1])
    answer = 0
    curr = -30001
    for start, end in routes:
        if curr < start:
            answer += 1
            curr = end
    return answer