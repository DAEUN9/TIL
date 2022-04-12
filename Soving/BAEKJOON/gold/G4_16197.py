# 두 동전
# https://www.acmicpc.net/problem/16197

import sys
sys.stdin = open('input.txt','r')

def game(coins, cnt):
    global min_cnt
    if cnt > 10:
        return
    if min_cnt <= cnt:
        return
    if len(coins)==1:
        min_cnt = cnt
    a = []
    for r, c in coins:
        if c-1>=0:
            if arr[r][c - 1] != '#':
                a.append((r, c-1))
            else:
                a.append((r, c))
    game(a, cnt+1)
    a = []
    for r, c in coins:
        if c+1<M:
            if arr[r][c+1] != '#':
                a.append((r, c+1))
            else:
                a.append((r, c))
    game(a, cnt+1)
    a = []
    for r, c in coins:
        if r-1>=0:
            if arr[r-1][c] != '#':
                a.append((r-1, c))
            else:
                a.append((r, c))
    game(a, cnt+1)
    a = []
    for r, c in coins:
        if r+1<N:
            if arr[r+1][c] != '#':
                a.append((r+1, c))
            else:
                a.append((r, c))
    game(a, cnt+1)

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
coins = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'o':
            coins.append([i, j])
min_cnt = 987654321
game(coins, 0)
if min_cnt == 987654321:
    print(-1)
else:
    print(min_cnt)