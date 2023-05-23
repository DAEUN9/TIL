import sys
sys.stdin = open("input.txt", "r")
n = int(input())
dp = [1]
for i in range(1, n+1):
    temp = 0
    for j in range(i):
        temp += dp[j]*dp[i-1-j]
    dp.append(temp)
print(dp[n])