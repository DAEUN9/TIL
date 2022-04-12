# 파이프 옮기기 2
# https://www.acmicpc.net/problem/17069


import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[False for _ in range(3)] for _ in range(N)] for _ in range(N)]
# 0: 가로, 1: 세로, 2: 대각선
for i in range(1, N):
    if arr[0][i]:
        break
    dp[0][i][0] = 1

for r in range(1, N):
    for c in range(1, N):
        if arr[r][c]:
            continue
        dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
        dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
        if arr[r - 1][c] == 0 and arr[r][c - 1] == 0:
            dp[r][c][2] = dp[r-1][c-1][2] + dp[r-1][c-1][0] + dp[r-1][c-1][1]

print(sum(dp[N-1][N-1]))