# 최대힙
# https://www.acmicpc.net/problem/11279
import sys
sys.stdin = open('input.txt','r')
import heapq
input = sys.stdin.readline
N = int(input())
a = []
for _ in range(N):
    curr = int(input())
    if curr:
        heapq.heappush(a, curr*-1)
    else:
        if a:
            print(heapq.heappop(a)*-1)
        else:
            print(0)