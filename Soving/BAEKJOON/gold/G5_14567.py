# 선수과목
# https://www.acmicpc.net/problem/14567

import sys
from collections import deque

# sys.stdin = open('input.txt','r')

input = sys.stdin.readline
v, e = map(int, input().split())

indegree = [0]*(v+1)

graph = [[] for _ in range(v+1)]
semester = [0] * (v + 1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            semester[i] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                semester[i] = semester[now] + 1


topology_sort()
print(*semester[1:])