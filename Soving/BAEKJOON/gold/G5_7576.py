import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

# 열 길이, 행 길이
M, N =map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for n in range(N)]
dq = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for n in range(N):
    for m in range(M):
        if arr[n][m] == 1:
            dq.append([n, m])
def bfs():
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]==0:
                dq.append([ny, nx])
                arr[ny][nx] = arr[y][x] + 1
bfs()
answer = 1
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            answer = -1
            break
        elif arr[i][j] > answer:
            answer = arr[i][j]
    if answer == -1:
        break
if answer > 0:
    print(answer-1)
else:
    print(answer)