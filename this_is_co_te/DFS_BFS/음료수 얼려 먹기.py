N, M = map(int, input().split())
visit = [[0]*M for _ in range(N)]
arr = [list(map(int, list(input()))) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(si, sj):
    stack.append([si, sj])
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] ==0 and not visit[nr][nc]:
                visit[nr][nc] = 1
                stack.append([nr, nc])

cnt = 0
stack = []
for i in range(N):
    for j in range(M):
        if arr[i][j] ==0 and not visit[i][j]:
            cnt += 1
            DFS(i, j)

print(cnt)
