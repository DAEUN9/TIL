import sys
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
t,p = [],[] # 시간, 금액액
dp = [0] * (n+1)
for i in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)
M = 0
for i in range(n):
    M = max(M,dp[i])
    if i+t[i] > n :
        continue
    dp[i+t[i]] = max(M+p[i],dp[i+t[i]])
print(max(dp))