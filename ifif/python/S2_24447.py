import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N, M, R = map(int, input().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort()
dq = deque()
dq.append([R, 1])
visited[R] = 1
answer = 0
idx = 1
while dq:
    e, depth = dq.popleft()
    for de in graph[e]:
        if not visited[de]:
            visited[de] = depth+1
            dq.append([de, depth+1])
            idx += 1
            answer += idx*(depth)

print(answer)
