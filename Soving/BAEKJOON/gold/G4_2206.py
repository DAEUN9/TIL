# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# N*M 행렬
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append(start)
    visited[0][0][1] = 1
    while q:
        r, c, cnt = q.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c][cnt]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc]=='1':
                    if cnt > 0 and not visited[nr][nc][cnt - 1]:
                        visited[nr][nc][cnt-1] = visited[r][c][cnt] + 1
                        q.append((nr, nc, cnt-1))
                elif not visited[nr][nc][cnt]:
                    visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                    q.append((nr, nc, cnt))
    return -1

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

start = (0, 0, 1)
answer = bfs()

print(answer)
