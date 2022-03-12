# N과 M (2)

import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
answer = []
def suyeol(i):
    if i==M:
        print(*answer)
        return
    for j in range(1, N+1):
        if answer==[] or answer[-1]<j:
            answer.append(j)
            suyeol(i+1)
            answer.pop()

suyeol(0)