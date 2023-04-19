def solution(n):
    global answer
    answer = 0
    for i in range(1, n+1):
        backtracking(n, i, i)
    return answer

def backtracking(n, total, num):
    global answer
    if total > n:
        return
    if total == n:
        answer += 1
        return
    backtracking(n, total+num+1, num+1)
        