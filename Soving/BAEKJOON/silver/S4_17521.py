import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, W = map(int, input().split())
coins = list(int(input()) for _ in range(n))

cnt = 0
answer = W
for i in range(n-1):
    if coins[i+1] > coins[i]:
        if answer // coins[i]:
            cnt = answer // coins[i]
            answer = answer % coins[i]

    elif coins[i-1] < coins[i] and cnt > 0:
        answer += cnt*coins[i]
        cnt = 0
print(answer + cnt*coins[n-1])

