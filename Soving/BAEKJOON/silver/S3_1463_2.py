import sys
sys.stdin = open("input_dt.txt", "r")

X = int(input())
dp = [1e9]*(X+1)
dp[0], dp[1] = 1, 0
for x in range(1, X+1):
    if x+1 <= X:
        dp[x+1] = min(dp[x+1], dp[x]+1)
    if x*2 <= X:
        dp[x*2] = min(dp[x*2], dp[x]+1)
    if x*3 <= X:
        dp[x*3] = min(dp[x*3], dp[x]+1)
print(dp[-1])