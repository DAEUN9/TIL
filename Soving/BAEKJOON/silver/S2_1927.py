# 최소 힙
# https://www.acmicpc.net/problem/1927

import sys
import heapq

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
hq = []
for n in range(N):
    a = int(sys.stdin.readline())
    if a:
        heapq.heappush(hq, a)
    elif hq:
        b = heapq.heappop(hq)
        print(b)
    else:
        print(0)