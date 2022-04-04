import sys
sys.stdin = open('sampleinput.txt','r')
T = int(input())
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r, c, word):
    global max_num
    q = []
    q.append((r, c))
    visited[r][c] = 1
    cnt = 1
    while q:
        cr, cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == word:
                visited[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))
    if max_num < cnt:
        max_num = cnt

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    Acnt = 0
    Bcnt = 0
    max_num = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'A' and not visited[r][c]:
                Acnt += 1
                BFS(r, c, 'A')
            elif arr[r][c] == 'B' and not visited[r][c]:
                Bcnt += 1
                BFS(r, c, 'B')
    print(f'#{t} {Acnt} {Bcnt} {max_num}')
