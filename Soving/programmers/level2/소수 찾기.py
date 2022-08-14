# 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
import math

def solution(numbers):
    numbers = list(numbers)
    answer = set()
    for i in range(1, len(numbers)+1):
        for num in list(map(''.join, permutations(numbers, i))):
            if primenumber(int(num)) and (int(num) not in answer):
                answer.add(int(num))
    return len(answer)

def primenumber(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
            return False
    return True