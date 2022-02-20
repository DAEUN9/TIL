import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
coins = [int(input()) for n in range(N)]
pay = 0
cnt = 0

for coin in coins[::-1]:
    if pay+coin > K:
        continue
    charge = K - pay
    pay += (charge//coin)*coin
    cnt += charge//coin
    if pay == K:
        break
print(cnt)
