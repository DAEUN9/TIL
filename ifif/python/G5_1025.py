# 제곱수 찾기
# 브루트포스

import sys
import math

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = [input() for i in range(N)]

def solution():
    max_val = -1

    for r in range(N):
        for c in range(M):
            for i in range(-N, N):
                for j in range(-M, M):
                    if i==0 and j==0:
                        continue
                    temp = ""
                    x, y = r, c
                    while 0<=x<N and 0<=y<M:
                        temp+=arr[x][y]
                        num = int(temp)
                        if math.sqrt(num).is_integer():
                            max_val = max(max_val, num)
                        x, y = x+i, y+j
    return max_val

print(solution())