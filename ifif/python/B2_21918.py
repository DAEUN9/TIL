# 전구
# 구현

import sys

sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
lights = list(map(int, input().split()))

def solution(a, b, c):
    if a == 1:
        lights[b-1] = c
        return
    if a == 2:
        for i in range(b-1, c):
            lights[i] = (lights[i]+1)%2
        return
    if a == 3:
        for i in range(b-1, c):
            lights[i] = 0
        return
    for i in range(b-1, c):
        lights[i] = 1
    return

for _ in range(M):
    a, b, c = map(int, input().split())
    solution(a, b, c)

print(*lights)

