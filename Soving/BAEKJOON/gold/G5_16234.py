# 인구 이동
# https://www.acmicpc.net/problem/16234

import sys
sys.stdin =open('input.txt', 'r')

from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# N*N 크기 땅 1칸씩 나라
# 인접 나라의 인구 차가 L명 이상, R명 이하라면 공유
N, L, R = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
li = deque()
for i in range(N):
    for j in range(N):
        li.append((i,j))
day = 1
while True:
    for _ in range(len(li)):
        r, c = li.popleft()
        if visited[r][c] == day:
            continue
        q = deque()
        q.append((r,c))
        total = arr[r][c]

        pos_list = [(r,c)]
        visited[r][c] = day
        while q:
            r, c =q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] != day:
                    if L<= abs(arr[nr][nc]-arr[r][c]) <= R:
                        visited[nr][nc] = day
                        total += arr[nr][nc]
                        q.append((nr, nc))
                        pos_list.append((nr, nc))
        cnt = len(pos_list)
        if cnt > 1:
            n = total // cnt
            while pos_list:
                i, j = pos_list.pop()
                arr[i][j] = n
                li.append((i, j))
    if li:
        day += 1
    else:
        break
print(day-1)