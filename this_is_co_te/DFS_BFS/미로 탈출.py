from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS():
    dq = deque()
    dq.append([0, 0])
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc]==1:
                arr[nr][nc] = arr[r][c] + 1
                dq.append([nr, nc])

BFS()
print(arr[-1][-1])
