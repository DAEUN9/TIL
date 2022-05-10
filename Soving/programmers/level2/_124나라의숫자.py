# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    _124 = ['4', '1', '2']
    answer = ''
    while n:
        curr = n%3
        n = n//3
        if curr == 0:
            n -= 1
        answer = _124[curr] + answer
    return answer
