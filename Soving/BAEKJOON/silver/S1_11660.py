# 구간 합 구하기5
# https://www.acmicpc.net/problem/11660

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 크기, 합횟수
N, M = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(N+1)]
for r in range(N):
    for c in range(N):
        dp[r+1][c+1] = dp[r][c+1] + dp[r+1][c] - dp[r][c] + arr[r][c]

for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    minus = dp[sr-1][ec] + dp[er][sc-1] - dp[sr-1][sc-1]
    total = dp[er][ec] - minus
    print(total)