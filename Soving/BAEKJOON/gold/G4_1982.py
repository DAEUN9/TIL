import sys
sys.stdin =open("input.txt", "r")

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def DFS(sx, sy, cnt, d):
    global res

    if res < cnt:
        res = cnt

    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]
        # 처음보는 알파벳이면
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] not in d:
            DFS(nx, ny, cnt+1, d+arr[nx][ny])



N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
res = 0
DFS(0,0,0, arr[0][0])
print(res+1)