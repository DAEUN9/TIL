# 그림
# https://www.acmicpc.net/problem/1926

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline



n, m = map(int, input().split())
grim = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
max_num = 0

def bfs(r, c):
    global max_num
    num = 0
    q = deque()
    visited[r][c] = 1
    q.append((r, c))
    while q:
        x, y = q.popleft()
        num += 1
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + i
            ny = y + j
            if 0<=nx<n and 0<=ny<m and grim[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

    if num > max_num:
        max_num = num

for i in range(n):
    for j in range(m):
        if grim[i][j] and not visited[i][j]:
            cnt += 1
            bfs(i, j)

print(cnt)
print(max_num)