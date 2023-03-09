import sys
from collections import deque
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
X, Y = map(int, input().split())
another = [list(map(int, input().split())) for _ in range(M)]
direction = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
dq = deque()
dq.append([X, Y, 0])
visited = [[0]*(N+1) for _ in range(N+1)]
visited[X][Y] = 1
while dq:
    x, y, cnt = dq.popleft()

    for a, b in direction:
        nx = a +x
        ny = b +y
        if 0<nx<=N and 0<ny<=N and not visited[nx][ny]:
            visited[nx][ny] = cnt+1
            dq.append([nx, ny, cnt+1])

for c, d in another:
    print(visited[c][d], end=" ")