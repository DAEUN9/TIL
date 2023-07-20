def solution(n, m):
    answer = [0, 0]
    for i in range(1, n+1):
        if n%i == 0 and m%i == 0:
            answer[0] = i
    for j in range(n, n*m+1):
        if j%m == 0 and j%n == 0:
            answer[1] = j
            break
    return answer