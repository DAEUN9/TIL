import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
miro = list(list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N))
dq = deque()
dq.append([0, 0])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and miro[nr][nc]==1:
                dq.append([nr, nc])
                miro[nr][nc] = miro[r][c] + 1
bfs()
print(miro)
print(miro[-1][-1])