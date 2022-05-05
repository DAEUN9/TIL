# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [0]*(N+1)
li = [0]+list(map(int, input().split()))
for n in range(1, N+1):
    dp[n] = dp[n-1]+li[n]

for _ in range(M):
    x, y = map(int, input().split())
    print(dp[y]-dp[x-1])