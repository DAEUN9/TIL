def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s*n
    return answer