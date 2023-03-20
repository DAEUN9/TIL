# 가장 긴 감소하는 부분 수열
#
# dp

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
A = list(map(int, input().split()))
dp = [0]*N

for i in range(1, N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp)+1)