def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j == n:
                answer += 1
            if i*j > n:
                break
    return answer