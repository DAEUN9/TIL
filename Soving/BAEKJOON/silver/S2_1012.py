# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque

# sys.stdin = open('input.txt','r')
#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())

def bfs():
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] and not visit[nr][nc]:
                visit[nr][nc] = 1
                dq.append((nr, nc))

for t in range(T):
    # 가로, 세로, 배추개수
    M, N, K = map(int, input().split())
    # 맵 만들기
    arr = list([0]*N for _ in range(M))
    visit = list([0] * N for _ in range(M))
    dq = deque()
    for k in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] and not visit[i][j]:
                cnt +=1
                dq.append((i, j))
                bfs()
    print(cnt)