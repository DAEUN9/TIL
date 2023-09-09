def solution(d, budget):
    d.sort()
    answer = 0
    curr = 0
    for i in d:
        if curr + i > budget:
            break
        curr += i
        answer += 1
    return answer