def solution(n):
    answer = 0
    while n:
        if n%2:
            answer += 1
        n //= 2
    return answer