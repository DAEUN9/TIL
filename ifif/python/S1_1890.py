import sys
from collections import deque

sys.stdin = open("input.txt", "r")
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
paths = [[0]*N for _ in range(N)]
paths[0][0] = 1

for x in range(N):
    for y in range(N):
        curr = arr[x][y]
        if curr == 0:
            continue
        if curr:
            if 0<=x+curr<N:
                paths[x+curr][y] += curr
            if 0<=y+curr<N:
                paths[x][y+curr] += curr
print(paths[-1][-1])