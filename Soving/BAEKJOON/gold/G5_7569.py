# 토마토
# https://www.acmicpc.net/problem/7569

import sys
sys.stdin = open('input.txt','r')
from collections import deque
input = sys.stdin.readline

d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def bfs():
    while q:
        h, r, c = q.popleft()
        for dh, dr, dc in d:
            nh = h + dh
            nr = r + dr
            nc = c + dc
            if 0<=nh<H and 0<=nr<N and 0<=nc<M and not visited[nh][nr][nc]:
                if arr[nh][nr][nc]!=-1:
                    visited[nh][nr][nc] = visited[h][r][c] + 1
                    q.append((nh, nr, nc))

def tomato():
    max_num = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if visited[h][n][m] == 0 and arr[h][n][m] != -1:
                    return False
                if visited[h][n][m] > max_num:
                    max_num = visited[h][n][m]
    return max_num

M, N, H =map(int, input().split())
visited = [[[0] *M for _ in range(N)] for _ in range(H)]
arr = []
q = deque()
for h in range(H):
    temp = []
    for n in range(N):
        temp.append(list(map(int, input().split())))
        for m in range(M):
            if temp[n][m]==1:
                visited[h][n][m] = 1
                q.append((h, n, m))
    arr.append(temp)
bfs()
answer = tomato()
if answer:
    print(answer-1)
else:
    print(-1)
