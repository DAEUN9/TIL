# 지능형 기차2
# https://www.acmicpc.net/problem/2460

import sys
sys.stdin = open('input.txt','r')

T = 10
curr = 0
max_people = 0
for _ in range(T):
    o, i = map(int, input().split())
    curr -= o
    curr += i
    if curr > max_people:
        max_people = curr
print(max_people)