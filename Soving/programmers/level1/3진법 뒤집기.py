def solution(n):
    answer = 0
    temp = ""
    while n >= 1:
        temp += str(n % 3)
        n //= 3
    for i in range(len(temp)):
        answer += int(temp[-i-1]) * 3**i
    return answer