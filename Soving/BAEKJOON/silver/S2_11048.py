import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]
dp = miro[:]

for i in range(N):
    for j in range(M):
        temp = 0
        if 0 <= i-1:
            temp = max(temp, dp[i-1][j])
        if 0 <= j-1:
            temp = max(temp, dp[i][j-1])
        if 0 <= i-1 and 0 <= j-1:
            temp = max(temp, dp[i-1][j-1])
        dp[i][j] += temp
print(dp[-1][-1])