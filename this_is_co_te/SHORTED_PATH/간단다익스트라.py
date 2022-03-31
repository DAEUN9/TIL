import sys
sys.stdin = open('01_input.txt', 'r')
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 N, 간선 개수 M
N, M = map(int, input().split())
start = int(input())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, N+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 노드에 대해 반복
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
for i in range(1, N+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])