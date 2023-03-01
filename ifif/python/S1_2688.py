# 줄어들지 않아
#
# dp

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1]*10
    for n in range(N-1):
        for i in range(10):
            dp[i] = sum(dp[i:])

    print(sum(dp))