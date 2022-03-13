import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 통로 행 길이, 열 길이, 음식물 쓰레기 개수
N, M, K = map(int, sys.stdin.readline().split())
trash_li = list(list(map(int, sys.stdin.readline().split())) for _ in range(K))
graph = list([0]*(M+1) for _ in range(N+1))

dq = deque()

for trash in trash_li:
    graph[trash[0]][trash[1]] = 1

def bfs():
    cnt = 1
    while dq:
        row, col = dq.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 1<=nr<N+1 and 1<=nc<M+1 and graph[nr][nc]==1:
                dq.append([nr, nc])
                graph[nr][nc] = 0
                cnt += 1
    return cnt
max_val = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j]== 1:
            dq.append([i, j])
            graph[i][j] = 0
            cnt = bfs()
            if max_val < cnt:
                max_val = cnt

print(max_val)