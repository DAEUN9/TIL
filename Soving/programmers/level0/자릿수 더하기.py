def solution(n):
    answer = 0
    for word in str(n):
        answer += int(word)
    return answer