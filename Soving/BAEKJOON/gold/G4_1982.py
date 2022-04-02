import sys
sys.setrecursionlimit(4000)
sys.stdin =open("input.txt", "r")

dx = [1,-1,0,0]
dy = [0,0,-1,1]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def DFS(sx, sy, cnt, d):
    global res
    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]
        # 처음보는 알파벳이면
        if 0 <= nx < N and 0 <= ny < M and not d.get(arr[nx][ny],0):
            # 알파벳 수집
            d[arr[nx][ny]] = 1
            # lis.append(arr[nx][ny])
            DFS(nx,ny,cnt+1, d)
            # 갔다왔으면 알파벳 삭제
            d[arr[nx][ny]] = 0
            # lis.remove(arr[nx][ny])
        # 갈곳 없으면 결과처리
        # else:
        elif res < cnt:
            res = cnt
            return

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
lis = dict()
lis[arr[0][0]]=1
visited = [[0]*M for _ in range(N)]
res = 0
DFS(0,0,0, lis)
print(res+1)