# 쉽게 푸는 문제
# https://www.acmicpc.net/problem/1292

import sys
sys.stdin = open("input.txt", "r")

def answer(A, B):
    result = [0, 0]
    idx = 0
    total = 0
    if B == 0:
        return 0
    for i in range(1, 1000):
        for j in range(i):
            idx += 1
            total += i
            if idx == A-1:
                result[0] = total
            if idx == B:
                result[1] = total
                return result[1] - result[0]

A, B = map(int, input().split())



print(answer(A, B))