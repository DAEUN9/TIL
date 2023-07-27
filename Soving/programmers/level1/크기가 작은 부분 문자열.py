def solution(t, p):
    n = len(p)
    answer = 0
    for i in range(len(t)-n+1):
        if int(t[i:i+n]) <= int(p):
            answer += 1
    return answer