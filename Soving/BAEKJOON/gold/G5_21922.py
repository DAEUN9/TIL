# 학부 연구생 민상
# https://www.acmicpc.net/problem/21922

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 연구실 세로 N, 가로 M
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
windy = []
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            windy.append((i, j))
            visited[i][j] = 1
            cnt += 1

def delta_check(r, c, nr, nc):
    if arr[nr][nc] == 1:
        return (r, 0)
    elif arr[nr][nc] == 2:
        return (0, c)
    elif arr[nr][nc] == 3:
        return (-c, -r)
    else:
        return (c, r)

def bfs():
    global cnt
    for r, c in windy:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = dr+r
            nc = dc+c
            while 0<=nr<N and 0<=nc<M and (dr or dc):
                if arr[nr][nc] == 9:
                    break
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    cnt += 1
                if 1<=arr[nr][nc]<=4:
                    dr, dc = delta_check(dr, dc, nr, nc)
                nr += dr
                nc += dc
bfs()
print(cnt)

