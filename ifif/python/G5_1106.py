# 호텔
#
# 다이나믹 프로그래밍
# 배낭 문제

import sys
sys.stdin = open("input.txt","r")
C, N = map(int,input().split())
cities = list(list(map(int, input().split())) for _ in range(N))
dp = [0] + [1e9]*C
for c in range(C):
    for cost, person in cities:
        if c+person < C:
            dp[c+person] = min(dp[c+person], dp[c]+cost)
        else:
            dp[C] = min(dp[C], dp[c]+cost)

print(dp[C])