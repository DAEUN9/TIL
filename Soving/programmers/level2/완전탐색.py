# 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        # i개 길이 중복순열
        for p in product(li, repeat = i):
            answer.append(''.join(p))
    answer.sort()
    return answer.index(word) + 1