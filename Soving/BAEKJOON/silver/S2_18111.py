# 마인크래프트
# https://www.acmicpc.net/problem/18111

import sys

sys.stdin = open('input.txt','r')
# 행, 열, 인벤토리에 있는 블록 수
N, M, B = map(int, input().split())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
min_time = 99999999999999
max_height = 0
total = 0
for i in range(N):
    total += sum(arr[i])
mean = total//(N*M)

for height in range(mean, 257):
    time = 0
    b = B
    for i in range(N):
        for j in range(M):
            if arr[i][j] < height:
                b -= (height - arr[i][j])
                time += (height - arr[i][j])
            elif arr[i][j] > height:
                b += (arr[i][j] - height)
                time += (arr[i][j] - height)*2
    if b < 0:
        continue
    if min_time >= time:
        min_time = time
        if max_height < height:
            max_height = height

print(min_time, max_height)