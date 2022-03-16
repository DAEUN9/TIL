# 주유소
# https://www.acmicpc.net/problem/13305

import sys

# sys.stdin = open('input.txt', 'r')

# 도시의 개수
N = int(input())
# 도로의 길이
paths = list(map(int, input().split()))
# 주유 리터당 가격
oils = list(map(int, input().split()))
curr = oils[0]
total = 0
for n in range(N-1):
    total += paths[n] * curr
    if oils[n+1] < curr:
        curr = oils[n+1]
print(total)