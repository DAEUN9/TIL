# 최소비용 구하기 2
# https://www.acmicpc.net/problem/11779

import sys
import heapq
sys.stdin = open('input.txt', 'r')

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] *(n+1)
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, goal = map(int, input().split())
move = [0] * (n+1)
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for i in graph[curr]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                move[i[0]] = curr
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
target = goal
print(distance[goal])
path = []
while target:
    path.append(target)
    target = move[target]


print(len(path))
print(*path[::-1])