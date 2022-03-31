import sys
import heapq

sys.stdin = open('01_input.txt', 'r')
input = sys.stdin.readline
INF = int(1e9)
# 노드의 개수, 간선의 개수
N, M = map(int, input().split())
start = int(input())
graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 짧은 노드에 대해 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])