import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(N):
    cnt = 0
    r,c = stack.pop()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        while 0<=nr<N and 0<=nc<N and path[nr][nc]==0:
            r = nr
            c = nc
            nr = r + dr[i]
            nc = c + dc[i]
        if r == 0 or c == 0 or r == N-1 or c == N-1:
            cnt += 1
        else:
            stack.append([r, c])



for t in range(1, T+1):
    N = int(input())
    cores = list(list(map(int, input().split())) for _ in range(N))
    path = list([0]*N for _ in range(N))
    stack = list()
    for i in range(N):
        for j in range(N):
            if cores[i][j] == 1:
                stack.append([i, j])


