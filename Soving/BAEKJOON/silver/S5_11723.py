# 집합
# https://www.acmicpc.net/problem/11723

import sys

sys.stdin = open('input.txt')

# 1. set() 이용한 풀이
# def calculator(word, x):
#     if word == 'add':
#         S.add(int(x))
#     elif word == 'remove':
#         S.discard(int(x))
#     elif word == 'check':
#         if int(x) in S:
#             print(1)
#         else:
#             print(0)
#     elif word == 'toggle':
#         if int(x) in S:
#             S.discard(int(x))
#         else:
#             S.add(int(x))
# N = int(input())
# S = set()
# for n in range(N):
#     li = sys.stdin.readline().split()
#     if len(li)>1:
#         calculator(li[0], li[1])
#     else:
#         if li[0] == 'all':
#             S = set([i for i in range(1, 21)])
#         else:
#             S.clear()

# 2. 비트마스킹 이용한 풀이
M = int(sys.stdin.readline())
S = 0b0

for m in range(M):
    li = sys.stdin.readline().split()
    if len(li)==1:
        if li[0] == 'all':
            S = 0b111111111111111111111
        elif li[0] == 'empty':
            S = 0b0
    else:
        li[1] = int(li[1])
        if li[0] == 'add':
            S = S|(0b1<<li[1])
        elif li[0] == 'remove':
            S = S & ~(0b1<<li[1])
        elif li[0] == 'check':
            if S & (0b1<<li[1]):
                print(1)
            else:
                print(0)
        else:
            S = S ^ (0b1<<li[1])