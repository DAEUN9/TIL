# 선발명단

# 브루트포스 알고리즘
# 백트래킹

import sys

sys.stdin=open("input.txt", "r")

C = int(input())
for _ in range(C):
    players = [list(map(int, input().split())) for _ in range(11)]
    positions = [0]*11
    status = 0
    def solution(idx):
        global status
        if idx == 11:
            status = max(status, sum(positions))
            return
        for i, player in enumerate(players, 0):
            if visited[i] or player[idx] ==0:
                continue
            visited[i] = 1
            positions[idx] = players[i][idx]
            solution(idx+1)
            visited[i] = 0
            positions[idx] = 0
    visited = [0]*11
    solution(0)
    print(status)