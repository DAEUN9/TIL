# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 정점 개수, 간선 개수
N, M = map(int, input().split())

li = [0]*(N+1)

def linked(n):
    q = deque()
    q.append(n)
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            if li[i]==0:
                li[i] = 1
                q.append(i)

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
total = 0
for i in range(1, N+1):
    if li[i] == 0:
        linked(i)
        total += 1

print(total)