N = int(input())
N = 1000 - N
cnt = 0
idx = -1
coins = [500, 100, 50, 10, 5, 1]
while N>=1:
    idx += 1
    cnt += N//coins[idx]
    N %= coins[idx]
print(cnt)