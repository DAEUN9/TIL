# 일루미네이션
#
# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 깊이 우선 탐색

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
W, H = map(int, input().split()) # 열, 행
buildings = [list(map(int, input().split())) for _ in range(H)]

direction_odd = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (1, 1)]
direction_even = [(-1, -1), (0, -1), (1, 0), (0, 1), (-1, 0), (1, -1)]
direction = [direction_odd, direction_even]
answer = 0
def bfs(c, d):
    dq = deque()
    dq.append([c, d])
    while dq:
        x, y = dq.popleft()
        for a, b in direction[x%2]:
            nx = x+a
            ny = y+b
            if 0<=nx<H and 0<=ny<W and not buildings[nx][ny]:
                buildings[nx][ny] = -1
                dq.append([nx, ny])

for i in [0, H-1]:
    for j in range(W):
        if not buildings[i][j]:
            buildings[i][j] = -1
            bfs(i, j)

for i in range(H):
    for j in [0, W-1]:
        if not buildings[i][j]:
            buildings[i][j] = -1
            bfs(i, j)

answer = 0
for k in range(H):
    for l in range(W):
        if buildings[k][l]!=1:
            continue
        temp = 0
        for a, b in direction[k%2]:
            nk = k + a
            nl = l + b
            if 0 <= nk < H and 0 <= nl < W:
                if buildings[nk][nl] == -1:
                    temp += 1
            else:
                temp += 1
        answer += temp

print(answer)