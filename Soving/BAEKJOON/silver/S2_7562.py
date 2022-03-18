# 나이트의 이동
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque

delta = [(-1,-2), (-1,2), (1,2), (1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

def bfs():
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            dx, dy = delta[i]
            nx = dx + x
            ny = dy + y
            if 0<=nx<I and 0<=ny<I and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                dq.append([nx, ny])
                if nx==t_x and ny==t_y:
                    return

sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(T):
    I = int(input())
    k_x, k_y = map(int, input().split())
    t_x, t_y = map(int, input().split())
    dq = deque()
    visit = [[0]*I for _ in range(I)]
    visit[k_x][k_y] = 1
    dq.append([k_x, k_y])
    bfs()
    print(visit[t_x][t_y]-1)

