# 최소비용 구하기
# https://www.acmicpc.net/problem/1916

import sys
import heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
N = int(input())
M = int(input())

INF = int(1e9)
# 플로이드 워셜
# graph = [[INF] * (N+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     graph[i][i] = 0
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
# start, end = map(int, input().split())
#
# for k in range(1, N+1):
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
#
# print(graph[start][end])

graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for i in graph[curr]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(distance[end])