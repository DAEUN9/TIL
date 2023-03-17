# 캠프가는 영식
#
# https://www.acmicpc.net/problem/1590
# 수학
# 브루트포스 알고리즘
# 이분 탐색

import sys
sys.stdin = open("input.txt", "r")
N, T = map(int, input().split())
def solution(T, S, I, C):
    start = 0
    end = C-1
    if S + C*I < T:
        return -1

    while start <= end:
        curr = (start + end) // 2
        if 0 <= S + curr*I - T < I:
            return S + curr*I - T
        if S + curr* I - T < 0:
            start = curr+1
        else:
            end = curr-1
    return S - T

answer = []
for _ in range(N):
    S, I, C = map(int, input().split())
    curr = solution(T, S, I, C)
    if curr >= 0:
        answer.append(curr)

if answer:
    print(min(answer))
else:
    print(-1)
