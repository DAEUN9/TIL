# 절댓값의 합
# https://www.acmicpc.net/problem/11286

import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())

heap = []
for i in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    elif heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)