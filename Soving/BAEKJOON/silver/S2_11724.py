import sys

sys.stdin = open('input.txt', 'r')

# 정점 개수, 간선 개수
N, M = map(int, input().split())

li = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)

